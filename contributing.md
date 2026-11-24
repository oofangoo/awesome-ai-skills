# Contribution guidelines

This list is a curation, not a collection. An entry belongs here only if someone has used the skill for real work and would recommend it.

## Adding a skill made by someone else

- Link to it. Do not copy it into this repo.
- One line, in this shape: `- [Name](link) - What it does, as a plain fact. By Author, licence.`
- The description starts with a capital letter and ends with a full stop. No slogans.
- Name the author and the licence. If the repo has no licence, say "no licence stated".
- Add it at the bottom of the section it fits. Open a new section only when three entries would go in it.
- Leave out anything unmaintained, archived or without instructions.

## Adding a skill to `skills/`

- One folder per skill, named in lowercase with hyphens, holding a `SKILL.md`.
- `SKILL.md` starts with front matter that has at least `name` and `description`. The description says what the skill does and when to use it.
- Keep it short: when to use it, the steps, the checks before calling the job done.
- If it uses an idea from someone else's work, add a `## Credits` section in the skill and a row in [CREDITS.md](CREDITS.md): the source, its author, its licence, what was taken and what was changed.
- Take the method, not the wording. Do not copy text unless the licence allows it, and then say so.
- No passwords, keys, private names, account names or anything about a real person.

## Before you open a pull request

- Check every link opens.
- Run `npx awesome-lint` and fix what it reports.
- One pull request per skill or per fix.
