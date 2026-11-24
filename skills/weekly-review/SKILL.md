---
name: weekly-review
category: learn
when: [review]
description: Close the week: read the results, update the plays, rewrite the strategy, tell the owner. Use once a week per channel.
version: 1
last_reviewed: 2026-11-23
---

# Weekly review

## Use this when

A week has passed since the last review. This is where a week of posts becomes something the channel knows.

## Steps

1. **Run the numbers.** `dcos brief --channel .` and `dcos score --channel . --write`.
2. **Take every reading that is due. Close every experiment that is ready.** Write each lesson as one line that says why, not what.
3. **Look at where you were most wrong.** Take the two experiments with the biggest gap between expected and result. What did you believe that was not true? That is the week's best lesson.
4. **Update the channel's plays.**
   - A play with a new held result: add the experiment to its `evidence`. Raise the grade only when the count allows it.
   - A play that failed again: note it. Three failures running: retire it.
   - Something that held twice with no play: write the play.
5. **Judge each bet by its own stop rule.** Keep, change or stop. Do not move the target after the fact.
6. **Check the five steps again.** Has the weak step moved? Is a different step now the weak one?
7. **Rewrite `strategy.md`** with the `strategy` skill.
8. **Offer what could help others.** Put findings, tool problems and skill gaps in `outbox/`.
9. **Write the owner's digest** at the top of `state.md`, 15 lines at most:
   - the numbers: posts shipped, how many beat the usual, the goal number
   - what we learned, in one or two lines
   - what changes next week
   - what you need from the owner

## Checks before you call it done

- No experiment past its window is still open.
- Every grade change has the experiments to back it. `dcos check` passes.
- The digest could be read on a phone in one minute.
- The review changed something: a play, a bet or a target. If nothing changed, say why.

## Good and bad

- Good: "3 of 5 beat the usual. Question openings held again (2.1× and 1.6×), now a proven play. Dropping long captions: 0.6× three times."
- Bad: "A solid week with good progress across several areas."

## Known problems

- (none yet)

## Results

- (none yet)
