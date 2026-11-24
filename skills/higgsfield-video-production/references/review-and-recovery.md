# Review the exported video

## Technical evidence

Use available local `ffprobe` and `ffmpeg` without installing software unnecessarily. The helper takes a local video and a new evidence directory:

```powershell
python 'SKILL_DIR/scripts/review_video.py' 'PROJECT/render.mp4' --out 'PROJECT/review-v1' --expected-seconds 20 --expected-ratio 9:16
```

Replace `SKILL_DIR` with this skill's actual installed directory and `PROJECT` with the current task's folder. The script refuses an existing evidence directory and leaves the input unchanged. It records metadata, a SHA256, full decode status, requested duration/aspect checks and sampled frames. Exit 2 means a technical check needs attention. `--at 6.5,7,7.25,7.5,8` targets a decisive interval; `--no-frames` skips image extraction.

An audio stream is evidence of a track, not evidence that the intended foley, speech or music is audible. File validity and sampled frames are not evidence of complete creative playback.

## Creative review

Watch the entire actual export using the available media preview or permitted browser playback. Seek around the important contact, transformation, cut or reveal; use dense frames to resolve a specific continuity question. Compare the result with the agreed brief:

- Does the intended action happen, and is its cause visible before the effect?
- Are identity, anatomy, shape, prop count, material and spatial relationships stable where the brief requires them?
- Do motion, contact, weight and travel agree with the intended physics and style? Does the camera preserve the information the scene needs?
- Are the opening readable, the ending delivered and the expressions/performances alive where relevant?
- For narration or demonstrations, are words, facts and the depicted process correct? Are captions readable if requested?
- Listen to the complete output where audible review is available. Record an honest audio-review limitation if it is not.

Do not fabricate playback, listening or acceptance. A contact sheet supports only the visible moments it contains. Deliver a partial-review verdict when the available surface cannot support the rest.

## Targeted revision

Name the observed failure and change the smallest useful variable: an ambiguous first frame, too many simultaneous actions, a hidden trigger, wrong camera framing, delayed contact or an unclear final consequence. If the problem is causal staging, speed changes alone may not repair it. Preserve source files and make a new version; distinguish an edit from a regenerated take. Recheck audio synchronization and the exported ending after any timing edit.

For a sequence, verify the assembled deliverable as well as its component clips. For a batch, record which items were actually reviewed and accepted rather than assigning one item's approval to its neighbors.
