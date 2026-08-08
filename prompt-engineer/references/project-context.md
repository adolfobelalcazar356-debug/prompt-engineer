# Project Context Reference

Use this reference when the optimized instruction depends on repository facts, project rules, or existing planning artifacts.

## Inspect before asking

For software work, discover facts in roughly this order, stopping as soon as enough context exists:

1. project instruction files such as `AGENTS.md` and `CLAUDE.md`;
2. relevant README or project-context files;
3. manifests/configuration such as `package.json`, `pyproject.toml`, language/framework config;
4. repository structure only as needed to locate the affected area;
5. relevant source code and tests;
6. `git diff` or change context when the request concerns existing modifications;
7. planning/specification artifacts that are directly relevant.

Do not ask the user what the repository can reliably answer.

## What belongs in persistent project context

Keep only **non-derivable** truths: facts the **code cannot safely tell** an agent by inspection alone.

Good examples:
- deliberate architecture decisions and rationale that constrain future changes;
- forbidden dependencies or deployment/runtime restrictions;
- compatibility commitments;
- organization/security/release constraints;
- known landmines;
- non-obvious conventions where the obvious alternative is intentionally wrong.

Avoid:
- directory inventories;
- generic framework descriptions;
- facts trivially visible in manifests/code;
- stale generated documentation.

## Context use rules

Treat executable code/config as the strongest evidence for mechanical facts. Treat prose as authoritative for human decisions only when it is current and relevant. If sources conflict in a way that changes the result, surface the conflict rather than silently choosing.

Do not copy large context documents into the optimized prompt. Extract only the load-bearing constraints needed by the executor.

## BMAD-aware behavior

BMAD is optional. Detect and **read/reuse** relevant artifacts when present, such as:

- `SPEC.md`;
- project-context artifacts;
- architecture outputs;
- stories or planning artifacts directly tied to the requested work.

Use existing BMAD decisions instead of recreating equivalent context. **Do not mutate** BMAD-owned artifacts in the MVP. Do not require BMAD installation/runtime, and do not force a BMAD workflow onto SIMPLE work.

If BMAD artifacts disagree with current code or with a newer explicit user instruction, do not hide the conflict. Preserve the user's current intent and route to clarification when the conflict materially affects scope or safety.

## Compression rule

The optimized prompt should carry decisions and constraints, not a miniature copy of the repository. If an executor can discover a fact cheaply and reliably, instruct it to inspect rather than embedding that fact as prose.
