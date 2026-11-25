---
name: make-image
category: make
when: [make]
description: Make still images with an AI image tool, and check them properly. Use for post images, covers and video frames.
version: 2
last_reviewed: 2026-11-25
---

# Make an image

## Use this when

You need a picture made by an AI image tool: a post image, a cover, a frame for a video.

## Steps

1. **Open `look.md` first.** Start from a reference piece's source: its first frame, its template, its prompt. Never from words alone. For a character who returns, give the tool an approved picture of that character every time.
2. **Say what the picture must show** in one line, and where it will be seen. The shape and crop come from the platform, so decide them first.
3. **Pick the tool** from `kit/tools/` by its "Best at" line.
4. **Use references for anything that returns.** A person, a place or a product that appears more than once gets approved reference pictures. For a place, fix a simple floor plan and move the camera, not the room.
5. **Write every prompt in full.** Never "same as before". Include:
   - who or what, and what they are doing
   - time of day, and where the light comes from
   - clothes and props, with counts
   - which way the camera faces, and what is behind it
   - the state of things: door open or shut, screen on or off
   - the style line, the same words every time
6. **Name things, not ideas.** "Four walls, a ceiling, the door shut" holds. "Enclosed" does not.
7. **No words or numbers inside the picture.** Add text afterwards with a real font: the `card-renderer` tool does this.
8. **Make more than one option.** With two tools, give both the same prompt and references. Retry a clearly broken result three times at most.
9. **Check at full size and at the final crop:**
   - hands, arms and faces join up
   - the right side of each object faces the camera (a laptop's lid, a phone's back)
   - the number of each prop
   - sizes against things at the same distance
   - things stand on something; hinges and edges make sense
   - light matches its source
   - clothes and props match the pictures before and after
   - the picture matches the words that go with it
10. **Fix the master first,** then make versions from it. After a small fix, check the whole picture again: a local fix can erase something else.
11. **Get a second look** from a reviewer who has not seen your verdict. It answers per picture: blocker, note, or could not verify.
12. **Write down** the prompt, the tool, the settings and which option won. Tool cards are improved from these.

## Checks before you call it done

- Checked at the real crop, not only the full frame.
- No generated text is visible anywhere.
- A second reviewer looked, and every blocker is fixed.
- The prompt and the winning tool are recorded.

## Known problems

- (none yet)

## Results

- Imported from one channel's correction history. These steps fixed problems the owner pointed out. No audience result is behind them yet.
