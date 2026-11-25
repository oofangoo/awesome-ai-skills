---
name: make-narrated-video
category: make
when: [make]
description: Cut a narrated video from still images, voice, captions and sound. Use for short videos and longer episodes built from stills.
version: 3
last_reviewed: 2026-11-25
---

# Make a narrated video from stills

## Use this when

The piece is a voice telling something over still pictures, short or long.

## Steps

1. **Open `look.md` first, and start from a reference piece's source:** its project file, render script or first frame. Reuse it; do not build a new template. A returning character is always generated from an approved picture of it, never from words alone, even when that costs more.
2. **Start from a script** made with `script-short-video` for short pieces. **Record the voice first, then measure it.** Build the timing from the real length of each line. A plan timed from the script can be far off.
3. **Check every voice line.** At least 0.3 seconds of silence at the end, so no word is cut. Level the speakers against each other. See the voice tool's card.
4. **Make each line fit its picture.** A line should end between 0.2 and 2 seconds before its picture does. If it runs over, rewrite the line shorter, three tries at most. Never speed the voice up. Trim the extra silence the voice tool adds.
5. **Check the plan is not a slideshow.** Before you render, rate it 0 to 5 on each: the same framing repeated; pictures that only decorate; motion with no reason; shots with no purpose you can name; too much text. If the average is 4 or more, fix the plan first.
6. **Still by default.** Move the camera only to reveal something, follow something or point at something, and give each move a place to arrive. Constant drifting reads as shake.
7. **Shake only for a physical hit,** in short bursts that fade out.
8. **Soften a hard join** with a short dissolve, 5 to 10 frames at 24 frames a second.
9. **Time each cue to the word that names it,** and to the loud point inside a sound effect, not the start of its file.
10. **Do not sit on one picture.** A hold past about 12 seconds needs a new picture or a move. Check for repeated framings as well as long ones.
11. **Keep music under the voice,** about 20 to 24 dB below it. Then listen in mono, with the music on and off. Music can pass a loudness check and still not be heard.
12. **Set the loudness of the finished file** to about -16 LUFS, with peaks under -1.5 dB. Measure the file you will ship, without filtering it again.
13. **Captions follow the final sound.** Take the timing from the recorded voice and the words from the script. Keep each caption short: about four words, 42 letters at most. Burn them in for short video. A translated track is timed to the audio it goes with.
14. **A tall version is a new cut.** Check every shot again after cropping.
15. **Check the finished file:** it plays from start to end; look at a frame every 2 seconds; captions cover every line; length and loudness are as planned; it plays and seeks in a real player.
16. **Say whether anyone listened.** If no agent could hear it, ask the owner for a listening check and say so in the experiment.

## Checks before you call it done

- A real, playable file exists, and step 14 passed on that file.
- Every number in your notes was measured on the shipped file.
- The opening follows the `hook` skill; the cover and title follow `packaging`.
- The fresh-eyes check ran on the finished file, not on the plan.

## Known problems

- (none yet)

## Results

- Imported from one channel's correction history and one owner's taste. No audience result is behind these steps yet. Treat the numbers as starting points.

## Credits

Steps 3 and 12 are adapted from the faceless-video skill in higgsfield-ai/skills (MIT). Step 4 follows an idea in OpenMontage (AGPL-3.0); no text or code was taken. See [CREDITS.md](../../CREDITS.md).
