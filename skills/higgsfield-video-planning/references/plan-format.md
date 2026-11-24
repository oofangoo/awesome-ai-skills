# Planning handoff

Use the smallest useful artifact set. A single clip can use one Markdown brief with an embedded shot record; a series benefits from a separate shot manifest and prompt files. Preserve any established project schema instead of converting it gratuitously.

## Brief fields

Record project and output purpose; audience and platform; requested duration and framing; visual mode; audio/language/text requirements; approved references; explicit constraints; chosen concept and ending; budget and generation authority; decisions made versus proposals; and what remains unknown.

## Shot record

The following example is a proposed shot, not a submitted job. Paths are relative to the project. Adapt the fields to the task.

```json
{
  "shot_id": "S01",
  "state": "planned",
  "timeline_seconds": [0, 8],
  "purpose": "Show the cup's instability before it is caught",
  "opening_state": "A cup stands near the tray's edge; a hand approaches from right",
  "event": "The tray tilts, the cup slides left, and the hand catches its handle before the edge",
  "ending_state": "Cup held upright; tray still tilted; no spill",
  "camera": "Medium side view keeps tray edge, sliding base and catching fingers visible",
  "references": [
    {"path": "inputs/cup.png", "role": "Cup shape and blue glaze; exclude the photographed background"}
  ],
  "audio": "Tray scrape, ceramic slide, quiet room; no speech or music",
  "prompt_file": "prompts/S01.txt",
  "requested_settings": {"duration_seconds": 8, "aspect_ratio": "16:9", "model": null, "resolution": null},
  "settings_verification": "not checked",
  "creative_checks": ["Tilt precedes slide", "Catch occurs before the edge", "Exactly one continuous cup"],
  "generation_authority": "planning only",
  "quoted_cost": null
}
```

An unknown value stays unknown. Do not invent model IDs, quotes, uploaded asset IDs or approval records. Approximate action timestamps guide a model; they are not frame-accurate guarantees.

For multiple shots, make the end of one shot and beginning of the next agree on identity, prop state, position, screen direction, light and audio. Separate planned total runtime from a model's individual clip limit. If stitching is required, name the transitions and assembly task rather than promising one native render.
