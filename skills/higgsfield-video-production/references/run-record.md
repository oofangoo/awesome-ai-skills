# Run records and recovery

Copy [the JSON template](../assets/run-record.json) into the task's output folder if the project lacks a suitable manifest. Extend the project's existing schema instead of maintaining two conflicting sources of truth.

Record relative project paths where practical, with stable shot and version identifiers. Keep the exact submitted prompt; reference roles and their local hashes or confirmed service IDs; requested settings; actual verified settings; route and generation authority; quoted cost and its observation time; returned job/result identity; source/master files and hashes; review evidence; and the remaining issue.

Use `null` or an explicit unknown state when a value was not observed. A visible creation timestamp is not necessarily a confirmed public-release timestamp. A model's ability to generate a format does not prove that this job used it.

Use operational states such as planned, prepared, handed_off, submitted, processing, completed, failed and outcome_unknown, as applicable. Keep these independent dimensions:

- Technical checks: not checked, pass or needs attention, with the actual findings.
- Creative review: not reviewed, partial, needs revision or reviewed, with evidence and limitations.
- User acceptance: unknown, pending, accepted or rejected, tied to actual user feedback and the exact version.
- Publication: not requested, draft, scheduled, published or unknown, with native verification if performed under a separate authorized task.

A technical pass does not advance user acceptance. Likewise, a user accepting a render does not establish publication or audience performance.

For a lost response, first search the known account/job history using the recorded prompt, settings, time and reference thumbnail. Do not assume a missing local file means the provider never submitted a job. Record what was reconciled and the reason for any new version.
