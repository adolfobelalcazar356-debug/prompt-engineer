# Prompt Engineer MVP — Downstream Evaluation Runbook

The six cases in `cases.json` are the first validation set. They are pressure/evaluation scenarios, not proof that the skill improves outcomes.

## Current status

All real agent executions are `PENDING_RUNTIME` until the cases are run in authenticated OpenCode, Codex, and/or Claude Code sessions. Do not infer a downstream win from static contract tests.

## Two-arm protocol

For each case, create two runs from the same clean repository state and, where possible, the same target agent/model/version:

### Arm A — original request

Send the case's **original request** directly to the executor without Prompt Engineer.

### Arm B — Prompt Engineer

Invoke Prompt Engineer explicitly, obtain the **Prompt Engineer output**, then hand that output to a fresh executor run. The optimizer must not execute its own handoff prompt.

Do not reveal Arm A results to Arm B or vice versa.

## Record these fields

For each arm record:

- `completion` — complete / partial / failed against the case's requested outcome;
- `unnecessary questions` — count questions whose answers were discoverable or irrelevant;
- `out-of-scope changes` — files/areas or behavior changed beyond the request;
- `invented requirements` — material requirements not supported by user/project context;
- `verification` — what tests/checks were actually run and their result;
- `follow-up iterations` — additional user turns required before an acceptable result;
- `prompt length` — characters or tokens for the original/optimized instruction;
- `route` — observed route when using Prompt Engineer;
- `notes` — qualitative evidence, including regressions or useful constraints.

## Case-specific checks

Use each case's `must_include`, `must_avoid`, `question_behavior`, and `expected_route` as an evaluation rubric. These are semantic expectations, not exact-string match requirements.

## First success threshold

Do not require Prompt Engineer to win every dimension. The MVP earns continuation if the six cases show useful downstream signal without systematic prompt bloat, especially on:

1. scope control in `PE-003`;
2. correct non-direct routing in `PE-004`;
3. critical clarification before destructive ambiguity in `PE-005`;
4. explicit risk/scope preservation in `PE-006`.

If SIMPLE work becomes materially longer without better execution, treat that as a regression even if the prompt looks more polished.

## Runtime record template

```text
case_id:
target_agent:
target_version:
model:
repo_revision:
status: PENDING_RUNTIME | COMPLETE
arm: ORIGINAL | PROMPT_ENGINEER
completion:
unnecessary_questions:
out_of_scope_changes:
invented_requirements:
verification:
follow_up_iterations:
prompt_length:
route:
notes:
```

Run each case from a reproducible starting state and preserve raw transcripts/diffs when available. Expand beyond these six cases only after the first cycle produces useful evidence.
