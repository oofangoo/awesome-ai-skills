---
name: paid-test
category: paid
when: [paid]
description: Spend a small ads budget as an experiment with a stop rule. Use when the charter has an ads cap and there is something worth spreading.
version: 2
last_reviewed: 2026-11-24
---

# Paid test

## Use this when

`channel.json` has an ads cap above zero, and you have a post that did well without ads, or one clear question money can answer.

## Steps

1. **Read the plays and warnings** for ads on this platform, and the ad tool's card.
2. **Decide what you are paying for.** Choose a result you can check later in ordinary behaviour, such as people who watch or share. A follow or like is not proof of an audience.
3. **Choose what to promote.** By default: the post with your best share rate without ads.
4. **Write the bet before any money moves.** Take the number you expect from this channel's own earlier test with the same goal, if there is one. Use an outside figure only when there is none, and write that it is a guess.
   `dcos bet --kind ad --metric cost_per_result --better lower --predict 0.50 --cost-money 5 …`
   In the experiment, also write:
   - the cap for this test, inside the monthly cap, counting tax and fees
   - the pass rule, for example "at least 30 results at 0.70 or less"
   - what a pass releases (the next, larger test) and what a fail means (stop)
5. **Start small.** A first test is a small share of the month's cap, for a fixed time. A pass earns the next stage. Nothing else does.
6. **Set it up as the tool card says.** One ad set. A fixed end. Publish it switched off, reload, read every field back, then switch it on. Do not edit it while it runs.
7. **Read the result:** spend, results, cost per result, and the split by where it was shown. Note the currency and how the platform credits a result. Then ask whether the count can be trusted: compare it with a second place, such as the post's own numbers, and treat the last few days as unfinished because results arrive late. If the count cannot be trusted, record "no reading": it is not a pass, not a fail, and it releases nothing.
8. **Judge by the rule you wrote.** Do not move the target afterwards.
9. **Do not chase the cheapest slice.** A group that looks cheap after the fact is a guess. Test it by itself before you believe it.
10. **Look a week later.** Did the people you paid for show up without ads: viewers on the next posts, shares, replies? Write that in the lesson.
11. **Close the experiment** with the real spend in `cost_money`, tax and fees included.
12. **Once a month, compare** the spend in the record with the platform's own billing page. If they differ, tell the owner.

## Checks before you call it done

- The pass rule is dated before the first spend.
- Total spend this month, with tax and fees, is inside the cap. `dcos check` agrees.
- The lesson says what the money bought in behaviour, not only in results.

## Good and bad

- Good: "Pass: 30 results at 0.70 or less in 24 hours releases a second test. Result: 19 at 2.50. Stopped."
- Bad: "The ad performed well, so I extended it."

## Known problems

- (none yet)

## Results

- Imported, one page, five tests: a cheap-looking slice cost 0.66 per result after the fact and 1.82 when tested alone. A cost target set too low nearly stopped delivery. Staged funding kept four failed tests to a small spend each.

## Credits

Steps 4 and 7 use two checks adapted from the ads references in marketingskills (MIT, © 2025 Corey Haines). See [CREDITS.md](../../CREDITS.md).
