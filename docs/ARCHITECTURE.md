# Architecture

## Product boundary

Prompt Engineer is a portable Agent Skill that converts a source request plus relevant context into a compact instruction for a downstream executor. It is not a full SDLC framework, autonomous multi-agent system, sprint manager, deployment system, or prompt database.

## Handoff-first execution

The canonical MVP separates optimization from execution:

```text
source request
    ↓
prompt-engineer
    ↓
route + context + constraints + verification
    ↓
optimized handoff prompt
    ↓
STOP
    ↓ (only after a separate user request)
executor
```

This boundary makes the optimized artifact inspectable and allows downstream evaluation against the original request.

## Canonical package

The installable package contains exactly seven files:

```text
prompt-engineer/
├── SKILL.md
├── references/
│   ├── software-engineering.md
│   └── project-context.md
├── adapters/
│   ├── opencode.md
│   ├── codex.md
│   └── claude-code.md
└── examples/
    └── examples.md
```

`SKILL.md` owns modes, routing, question policy, readiness, output discipline, and progressive-loading directions.

The two references contain heavier reusable guidance. The three adapters contain only host-specific discovery/invocation details and execution emphasis. Examples demonstrate output shape without becoming templates.

## Routing

Prompt Engineer makes one lightweight decision based on:

- task intent;
- complexity;
- critical missing context;
- execution route.

Complexity levels:

- **SIMPLE** — localized, clear, low blast radius;
- **BOUNDED** — clear goal with meaningful implementation risk or multiple affected areas;
- **COMPLEX** — architectural impact, multiple independent deliverables, or unresolved product/technical decisions.

Routes:

- `EXECUTE_DIRECTLY`
- `EXPLORE_FIRST`
- `PLAN_FIRST`
- `SPEC_FIRST`
- `ASK_USER`

Readiness is a final check, not a separate workflow engine.

## Question policy

Inspect before asking. Questions are normally zero and never more than two. A question is justified only when different answers materially change scope, safety, data impact, or the requested outcome and the answer cannot be reliably discovered from the supplied artifacts/repository.

## Project context

Persistent project context should contain non-derivable truths: architecture decisions, forbidden dependencies, compatibility commitments, organization constraints, release restrictions, known landmines, or intentional conventions.

The optimized prompt should not become a miniature repository dump. If a fact can be discovered cheaply and reliably, instruct the executor to inspect it instead of embedding it.

## BMAD awareness

BMAD is optional. Relevant BMAD artifacts may be read and reused. Prompt Engineer does not require BMAD, does not mutate BMAD-owned artifacts in the MVP, and does not force BMAD workflows onto SIMPLE requests.

## Evaluation philosophy

Prompt aesthetics are not the primary metric. Compare downstream runs using completion, unnecessary questions, out-of-scope changes, invented requirements, verification performed, follow-up iterations, and prompt length.
