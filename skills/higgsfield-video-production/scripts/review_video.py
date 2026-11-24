#!/usr/bin/env python3
"""Read-only video QC with fresh evidence files; no creative or approval verdict."""

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess


def command(args, timeout=300):
    result = subprocess.run(args, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=timeout)
    return result.returncode, result.stdout, result.stderr


def numeric(value):
    try:
        number = float(value)
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def ratio(value):
    try:
        result = float(Fraction(value.replace(":", "/")))
        return result if math.isfinite(result) and result > 0 else None
    except (AttributeError, ValueError, ZeroDivisionError):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", required=True, type=Path,
                        help="New directory; existing evidence is never overwritten")
    parser.add_argument("--expected-seconds", type=float)
    parser.add_argument("--tolerance", type=float, default=0.15)
    parser.add_argument("--expected-ratio", help="For example 9:16 or 16:9")
    parser.add_argument("--at", help="Comma-separated sample seconds")
    parser.add_argument("--no-frames", action="store_true")
    args = parser.parse_args()
    source, output = args.video.resolve(), args.out.resolve()
    if not source.is_file():
        parser.error("Input is not a local file")
    if output.exists():
        parser.error("Evidence directory already exists; choose a new path")
    if not math.isfinite(args.tolerance) or args.tolerance < 0:
        parser.error("Tolerance must be finite and nonnegative")
    if args.expected_seconds is not None and (
            not math.isfinite(args.expected_seconds) or args.expected_seconds <= 0):
        parser.error("Expected duration must be finite and positive")
    expected_ratio = ratio(args.expected_ratio) if args.expected_ratio else None
    if args.expected_ratio and expected_ratio is None:
        parser.error("Expected ratio must be positive, such as 9:16")
    selected = None
    if args.at:
        try:
            selected = sorted(set(float(item.strip()) for item in args.at.split(",")))
        except ValueError:
            parser.error("Sample times must be comma-separated numbers")
        if any(not math.isfinite(t) or t < 0 for t in selected):
            parser.error("Sample times must be finite and nonnegative")
    ffprobe, ffmpeg = shutil.which("ffprobe"), shutil.which("ffmpeg")
    if not ffprobe or not ffmpeg:
        parser.error("ffprobe and ffmpeg must already be available on PATH")

    output.mkdir(parents=True, exist_ok=False)
    report = {
        "source": str(source), "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "technical_status": "needs_attention", "checks": {}, "issues": [],
        "review_frames": [], "creative_review": "not_performed",
        "audio_listening": "not_performed", "user_acceptance": "unknown"
    }
    digest = hashlib.sha256()
    with source.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    report["sha256"] = digest.hexdigest()
    try:
        code, stdout, stderr = command([
            ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(source)
        ])
        if code:
            raise ValueError("ffprobe failed: " + stderr[-2000:])
        metadata = json.loads(stdout)
        (output / "ffprobe.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        streams = metadata.get("streams", [])
        video = next((s for s in streams if s.get("codec_type") == "video"
                      and not s.get("disposition", {}).get("attached_pic")), None)
        if not video:
            raise ValueError("No playable video stream found")
        video_map = f"0:{video['index']}"
        audio = [s for s in streams if s.get("codec_type") == "audio"]
        duration = numeric(metadata.get("format", {}).get("duration"))
        if duration is None:
            duration = numeric(video.get("duration"))
        fps = ratio(video.get("avg_frame_rate", ""))
        width, height = int(video.get("width", 0)), int(video.get("height", 0))
        sar = ratio(video.get("sample_aspect_ratio", "")) or 1.0
        actual_ratio = width * sar / height if height else None
        report.update({"duration_seconds": duration, "width": width, "height": height,
                       "fps": fps, "display_ratio": actual_ratio,
                       "sample_aspect_ratio": video.get("sample_aspect_ratio"),
                       "video_codec": video.get("codec_name"), "has_audio_stream": bool(audio),
                       "audio_codecs": [s.get("codec_name") for s in audio]})
        code, _, stderr = command([
            ffmpeg, "-v", "error", "-xerror", "-i", str(source),
            "-map", video_map, "-map", "0:a?", "-f", "null", "-"
        ])
        report["checks"]["complete_decode"] = code == 0
        if code:
            report["issues"].append("Full decode failed: " + stderr[-2000:])
        if args.expected_seconds is not None:
            report["checks"]["requested_duration"] = (
                duration is not None and abs(duration - args.expected_seconds) <= args.tolerance)
            report["expected_seconds"] = args.expected_seconds
            report["duration_tolerance_seconds"] = args.tolerance
        if expected_ratio is not None:
            report["checks"]["requested_ratio"] = (
                actual_ratio is not None and abs(actual_ratio / expected_ratio - 1) <= 0.01)
            report["expected_ratio"] = args.expected_ratio
        if not args.no_frames:
            if duration is None or duration <= 0:
                raise ValueError("Known positive duration required to select review frames")
            if selected is None:
                last = max(0.0, duration - (1 / fps if fps else 0.1))
                selected = [last * i / 7 for i in range(8)]
            if any(t >= duration for t in selected):
                raise ValueError("Sample time is outside the video's duration")
            for index, seconds in enumerate(selected, 1):
                frame = output / f"frame-{index:02d}-{seconds:.3f}s.png"
                code, _, stderr = command([
                    ffmpeg, "-v", "error", "-n", "-ss", str(seconds), "-i", str(source),
                    "-map", video_map, "-frames:v", "1", str(frame)
                ])
                if code or not frame.is_file():
                    raise ValueError("Frame extraction failed: " + stderr[-1000:])
                report["review_frames"].append({"seconds": seconds, "file": frame.name})
        if report["checks"] and all(report["checks"].values()) and not report["issues"]:
            report["technical_status"] = "pass"
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        report["issues"].append(str(exc))
    (output / "technical-review.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"technical_status": report["technical_status"],
                      "report": str(output / "technical-review.json"),
                      "frame_count": len(report["review_frames"]),
                      "creative_review": report["creative_review"],
                      "user_acceptance": report["user_acceptance"]}))
    return 0 if report["technical_status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
