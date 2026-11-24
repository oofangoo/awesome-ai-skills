---
name: ship-and-verify
category: ship
when: [ship]
every_piece: yes
description: Publish or schedule a piece, then prove that what went live is what you made. Use every time something ships.
version: 1
last_reviewed: 2026-11-23
---

# Ship and verify

## Use this when

A piece has passed the fresh-eyes check and is cleared to ship: the format is `auto`, or the owner has approved it.

## Steps

1. **Check you may.** The approval is recorded with a link to the owner's words, or `channel.json` sets this format to `auto`. Otherwise ask the way the channel has agreed, and wait. One easy way: save the piece as a draft in the scheduling tool; the owner moving it to the queue is the yes.
2. **Check the account.** The name on screen matches the charter.
3. **Check for a double.** Look at the live channel, the schedule queue and the record. The same piece must not already be there. If an earlier try ended unclear, find out what happened before you try again.
4. **Upload the media first,** then the words. A link pasted first can turn into a link preview and replace your image.
5. **Save it,** scheduled or live.
6. **Read it back.** Reopen what you saved and compare with your file: the words, the date and time, how many images and in what order, alt text, captions, links.
7. **"Scheduled" is not "published".** Record it as scheduled. Do not start the clock yet.
8. **After it goes live, look at the real thing:** open the public link, in the real feed layout, at phone size. Check the crop, the words and that it plays. A preview is not proof.
9. **Record it:** `dcos ship` with the public link and the time it went live. The reading ages count from here.
10. **Note it in `state.md`** under "In flight".

## Checks before you call it done

- The experiment has the public link and the real time it went live.
- You saw the live piece yourself, not only the tool's preview.
- Nothing shipped twice.
- An approval you rely on can be opened by anyone reading the record.

## Good and bad

- Good: "Scheduled for Tuesday 09:05. Read back: text matches, 3 images in order, alt text present. Not yet live."
- Bad: "Posted." (Was it? Where is the link? Did the crop hold?)

## Known problems

- (none yet)

## Results

- Imported from one page's publishing steps. Reading back caught changed dates, a wrong image count and two cropped covers that the scheduling tool's preview had shown as fine.
