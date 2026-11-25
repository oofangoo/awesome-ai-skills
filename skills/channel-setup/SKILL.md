---
name: channel-setup
category: plan
when: [setup]
description: Onboard a channel with the owner so it can then run by itself, one step at a time - diagnose what works from where you run and give the owner one list to switch on, audit and research, agree the charter, wire every route, plan from proven posts, start the workflows, prove one piece. Use while channel.json says setup.
version: 8
last_reviewed: 2026-11-25
---

# Channel setup

## Use this when

`channel.json` says `"status": "setup"`. Setup is done **with the owner**, over as many sittings as it takes. When it ends, the channel runs with no input from the owner except a short agreed list.

**Start every sitting with `dcos next --channel .` and do the step it names: all of it, without waiting to be told.** Then run it again and go straight on to the next step. Stop only for a hard stop, something only the owner can do, or a decision that is the owner's (`START.md`, "Run from start to finish"). Each step needs the one before it, so never skip ahead. `dcos bet` refuses to plan a piece before the charter is agreed and the routes work.

## How to work with the owner

- **Homework first.** Read every old record, audit and research before you ask anything. Ask only what you cannot work out.
- **Bring a recommendation, never a bare question.** "I recommend X, because Y. Yes?"
- **One decision sheet, not a string of questions.** Every decision you need goes on one page, each with your recommended answer. The owner answers once.
- **Write the answer where it lives, in the same sitting.** What the owner decides is the owner's word. Put it in `charter.md` or `channel.json`, commit as `[owner]`, and quote the owner's words in the commit. Do not park it in a note.
- **Say it short.** What you found, what you recommend, what you need. Lead with the answer. Ten lines; the page behind it holds the rest.
- **Evidence, best first:** this channel's own numbers, when they are big enough to read; proven posts of comparable accounts, with their numbers; the platform's own guidance. General studies come last and never decide anything alone.
- **Make nothing before part 5.** No drafts, pictures or test designs until the charter is agreed.

## Part 1. Diagnose yourself

The owner may run you in any app. So the first job is to find out what you can do from where you are, and to hand the owner one list of what to switch on. Do this again whenever you are started somewhere new.

1. **Read what exists:** old brand notes, decisions and plans. List the owner's standing decisions. They go on the decision sheet in part 2 as keep, change or drop.
2. **Write where you run,** in `access.json` under `runs_in`. Only you can see your own tools: the app's name, the kind of session, whether you have a shell, every browser and way of controlling one that you have (a built-in one, a cloud one, an extension, desktop control) and whether each can stay signed in, each connector you can call, whether you can run on a schedule, whether your files last. Look at your real tool list. Do not answer from memory.
3. **List the platforms in view** under `in_view`: every platform the channel has an account on or is considering, with `has_account`.
4. **Read the tool cards first** (`kit/skills/INDEX.md`, "Tools by job"). They say which routes exist for a tool and what the owner must do once.
5. **Try every job from here,** for each platform in view:
   - **research:** look around inside the platform as a reader does. Open three comparable accounts and read their latest posts with the numbers under them. Search the subject. Read comments. Research is done in the platform, not about it.
   - **measure:** read one of the channel's own numbers and compare it with the platform's own page
   - **publish:** make a draft, read it back, delete it
   Then the other jobs the channel will need: reply, make-image, make-video, voice, edit, store, ads.
6. **Do not stop at the first route that fails, and do not ask the owner to choose.** If you have three browsers, try all three before you say the browser route failed. A note from an earlier sitting that names one tool does not limit you to it. Try each kind in turn: a connector; a key or API; a command-line tool; a browser; the owner by hand. A key the owner makes once on the platform works in any app that has a shell and a place to keep secrets, so when the connector is missing and the browser fails, the key is next.
7. **Write one entry in `access.json` for every route you tried,** the failed ones too. One tool and one kind of route per entry; `tool` is the tool card's name where there is a card. A route that works gets `status: working`, `tested_at`, `test` (what you did and saw) and `tested_from`: the app's name, exactly as in `runs_in`. A route marked working from another app does not count: try it again here.
8. **Write `needs_owner` only when there is something the owner can do now:** where to go, what to switch on or sign in to, how long it takes, how you will confirm it. "Pending" and "if supported" are not actions: find out first. Never describe a menu or button you have not confirmed exists in this app. If you cannot confirm it, say "I cannot see your screen" and ask what the owner sees.
9. **Say a dead end out loud.** If no kind of route can work from this app, leave `needs_owner` empty, write why in `test`, and give the owner the choice: another kind of route, or doing that one job from another app.
10. **Run `dcos doctor --channel . --write`** and send the owner `work/owner-actions.md` as one message, the urgent part first. Never type a password or key yourself. When the owner has acted, try again and run the doctor again.
11. **Articles and studies are no substitute.** If no route into a platform works yet, the stopgap is the owner sending 10 to 15 links or screenshots from inside it. Say plainly that it is a stopgap. Do not start part 2 on web searches alone.

## Part 2. Audit, research, proven posts

5. **Audit what exists** (`channel-audit`), and backfill the old posts. End on one sentence: is it that nobody sees the posts, or that people see them and do not care?
6. **Research the field** (`niche-research`): is the audience there, who serves them, the gap, what it takes, the odds.
7. **Study proven posts** (`find-what-works`). `work/outliers.md` needs at least 5 rows, each with a link, a ratio, and how the post is built.
8. **Write the decision sheet,** `work/decision-sheet.md`, one page:
   - what you found, in five lines, and where it disagrees with the owner's first intent
   - what you recommend: the reader, the platform, the formats, the goal and its date
   - the decisions, numbered: the question, your answer, one line of why, and a blank for the owner's answer. Cover the standing decisions, the goal and checkpoints, platforms, formats and rhythm, where real material will come from, money for tools and ads, autonomy, and what reaches the owner.
9. **Bring it to the owner.** Record each answer on the sheet and in `research.md`. Remove the template line.

## Part 3. Agree the charter

10. **Write `charter.md` and `channel.json` from the answers.** One platform to start. One or two formats, at a rhythm that can be kept up. One number and one date, with 30- and 90-day checkpoints. The monthly caps. `approve-each` or `auto` for every format. What reaches the owner, and where.
11. **Name the material.** What real things will the pieces be made from: things that happened, readers' questions, the channel's own numbers, public sources? And why would a stranger listen to this account? A channel with neither makes posts anyone could have made.
12. **Write the house look, `look.md`.** Start from what is already published or approved: open the pieces, not notes about them. List them as reference pieces, with where each one's source files are kept. Write what stays the same (art style, characters, colours, type, layout, sound) and what never appears. Add the owner's earlier style decisions. A new channel with nothing published yet makes one sample piece for this, and the owner picks.
13. **Read both back.** Commit `charter.md`, `channel.json` and `look.md` as `[owner]` after the owner's yes. Remove the template lines.

## Part 4. Wire and test every route

14. **List the jobs this channel needs:** publish, measure, reply, make-image, make-video, voice, edit, store, ads, research.
15. **Pick a tool for each** from `kit/tools/` by its "Best at" line and cost. **Pick the route, best first:** a connector the owner approves once; a key or API; a command-line tool signed in where the agent runs; a signed-in browser; the owner by hand. By hand is a stopgap, never for publishing or measuring.
16. **Write each route in `access.json`,** and give the owner the one-time steps as one list. No password, key or token goes in the chat or a repo.
17. **Test every route for real,** from the place and the agent that will do the work, and write `tested_from`. If the scheduled workflows will run in another app than this conversation, test from there too:
    - **read:** fetch a number you can also see on the platform's own page, and compare
    - **write:** create a draft, private or unlisted item, read it back, delete it
    - **make:** produce one real piece and check it
    - **ads:** read-only first
    Mark it `working` only then, with the date and what you did and saw. Give each must-have job a fallback.
18. **Settle two things that are easy to miss.** Where finished pictures and video get a public web address, if the publishing tool needs a link. And how the owner says yes to a piece that is not `auto`.

## Part 5. Plan from proven posts

19. **Write `strategy.md`** (`strategy`): the weak step, one to three bets, and the format sheet.
20. **Write `plan.md`** (`content-plan`), and record the first week's bets.
21. **Make the first pieces** (`model-a-proven-post`), each from a row in `work/outliers.md`.
22. **Send the owner the review sheet:** each piece next to the post it is modelled on. One message, one answer.

## Part 6. Start the workflows

23. **The channel runs as a few scheduled workflows,** each with a standing instruction in `workflows/`:

    | Workflow | Does | Usual rhythm |
    |---|---|---|
    | `drive` | Measures, makes and ships what the plan has for today | Daily, or as often as the channel posts |
    | `replies` | Answers real comments | Once or twice a day, if there are comments |
    | `review` | Closes the week, updates plays, rewrites the strategy and plan, sends the digest | Weekly |
    | `audit` | Re-tests every route, refreshes the research and the proven posts, checks the checkpoints | Monthly |

24. **Adjust the instructions** in `workflows/` with the owner. They are the owner's pages: commit as `[owner]` after a yes.
25. **Create one scheduled task per workflow** in the app the agent runs in. Its prompt is one line: "Read `workflows/<name>.md` in [repo] and do it." Give it the repos and connectors that workflow needs, and nothing more.
26. **Watch each one run once by itself.** It must start on time, in the right time zone, reach the repos and tools, and push. Write the schedule in `access.json` with `tested_at`.

## Part 7. Prove it end to end

27. **Take one real piece per format through the whole loop:** bet, make, fresh-eyes check, the owner's yes, ship, and a reading a day later. Put the experiment's id under `end_to_end` in `access.json`.
28. **Run `dcos ready --channel .` until it passes.** Then the owner sets `"status": "active"`.

## Part 8. Hand over

29. Bring `state.md` up to date. Tell the owner in a few lines what now runs by itself and when, and what will still reach them.
30. Leave a note in `outbox/` for every route and schedule you tested: what worked, what did not, with dates.

## Checks before you call it done

- `dcos ready --channel .` passes.
- The owner answered one decision sheet, and every answer is in the charter or `channel.json`.
- Every first piece was shown next to the proven post it is modelled on.
- Publishing, measuring and looking around inside each platform work with no owner and no hand-typed step, from where they will run.
- No password, key or token is in the repo or the chat.

## Known problems

- 2026-11 (import): a browser route lost its sign-in and an agent logged failed attempts daily for two weeks. Prefer connectors and keys; give every must-have job a fallback.
- 2026-10 (import): a schedule was read in the wrong time zone and reviews ran up to 43 hours late. Watch the first run.
- 2026-10 (import): a schedule on a personal computer stops when that computer is off. Prefer one that runs in the cloud.
- 2026-11-24: a command-line tool whose sign-in opens a browser on the same machine could not be signed in on a cloud machine. Check where a sign-in must happen before choosing the route.
- 2026-11-24: a scheduled task that starts a fresh session each time had no access to the repo and did nothing. Check the first scheduled run can pull.
- 2026-11-24: an agent asked the owner one small question after another, then made six pieces before it had read one competitor's post. The owner had to turn it back five times. Hence `dcos next`, the decision sheet and "make nothing before part 5".
- 2026-11-24: an agent could not open other accounts' posts where it ran, and used news articles and studies in their place. The owner called the pieces bland. Hence part 1, steps 5 and 11.
- 2026-11-24: the app an agent ran in had no publishing connector and no working browser. The routes were marked `working` from tests in a different app, so nothing warned it until the first piece was due to ship. Hence part 1: the agent diagnoses itself wherever it is started.
- 2026-11-24: an agent whose browser failed wrote every platform job as a browser route and gave the owner "pending a working connection" three times. It never tried the key route, which its app could have used. It also told the owner to use a menu the owner's app does not have, twice. Hence part 1, steps 6, 8 and 9.
- 2026-11-25: two channels made pieces that did not look like anything they had published. Neither had its look written down in one place: one had it only in an old decision note, one had a playbook that allowed "photorealistic or cartoon". Hence step 12 and `look.md`.
- 2026-11-24: an agent opened with only a repo link asked what the owner wanted, though `state.md` said. Told to resume, it tried one browser, then told the owner to start another chat and paste a prompt; then asked the owner to open a page and read out a name. The built-in browser it had listed worked first time, once the owner named it. Then it stopped after one check and waited for "keep going". Six steers in one sitting. Hence `START.md`, "Run from start to finish", and step 6.

## Results

- (none yet)
