---
name: measure
category: learn
when: [measure]
every_piece: yes
description: Read a post's numbers at the right age and record them honestly. Use every session that has readings due.
version: 1
last_reviewed: 2026-11-23
---

# Measure

## Use this when

`dcos brief` lists a reading as due, or you are about to close an experiment.

## Steps

1. **Know the numbers before you look.** Each experiment names one main number (`metric`). Read up to three more that explain it, for example for a short video: views, the share who stayed past the opening, shares.
2. **Take the public numbers first.** Views, likes, comments and shares that show on the public page need no sign-in. Any agent can read them. The platform's tool card lists which numbers are public.
3. **Then the signed-in numbers,** from the platform's own insights page. Check the account name on screen first.
4. **Read at the set ages:** 24 hours and 7 days, or what `channel.json` says. If you are late, read anyway. The script records the post's real age.
5. **Record it:** `dcos read --channel . ID --source public views=120 shares=3 stayed=na`.
6. **Keep a screenshot** in `work/evidence/` for signed-in numbers.
7. **Close at the window.** `dcos close` with the main number. The script works out the verdict.

## Rules for honest numbers

- **Missing is `na`, never 0.** A real zero stays 0. A dash on screen is `na`.
- **Keep different counts apart.** Views are not viewers, reach or impressions. A view is not a person. Some platforms count a view in more than one way: the platform's tool card says which number to use.
- **Like with like.** Compare the same platform, format, number and age. A photo's view and a video's view are different events.
- **Write the window and the time zone** of any report you read. A live count and a processed total on the same day can differ several times over.
- **A rate needs both halves from the same window.**
- **Do not credit one post for follower change.** Followers are the end count minus the start count.
- **Keep paid and unpaid apart.**
- **Tiny counts lie.** Your own visits show up in them. Under about 20, say "too few to read".

## When you cannot read a number

1. Record it as `na` and write why in `state.md`.
2. Try again next session. Public numbers do not depend on the sign-in.
3. Two sessions in a row without the signed-in numbers: ask the owner to read the three you need. That takes two minutes and keeps the record whole.

## Checks before you call it done

- Every reading has a source and an age.
- No blank was typed as 0.
- The number you closed on is the one named in the bet.

## Known problems

- (none yet)

## Results

- Imported from two channels' measuring rules. Both lost weeks of readings when a signed-in browser stopped working; steps 2 and "When you cannot read a number" are the answer to that.
