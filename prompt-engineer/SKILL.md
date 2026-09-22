---
name: prompt-engineer
description: Use when a user needs a request optimized, audited, explained, or compared before handing it to OpenCode, Codex, Claude Code, or another AI agent, especially when scope, context, requirements, or risk are unclear.
license: MIT
---

# Prompt Engineer

## Core principle

Produce the shortest instruction that preserves what an executor needs for correct, bounded, verifiable work. Preserve intent; do not invent requirements or add ceremony for its own sake.

## Invocation and handoff

The MVP uses explicit invocation and a handoff model: optimize or audit the request, return the requested artifact, then stop. Do not execute the optimized prompt yourself unless the user asks for direct execution as part of the task.

Automatic prompt-quality activation is out of scope for the MVP. Host-native discovery may exist, but correctness must not depend on implicit invocation.

## Modes

- `optimize` — default. Return only the final prompt.
- `audit` — return a compact readiness review: strengths, blocking gaps, risks, and recommended route.
- `explain` — `optimize` output variant: final prompt plus brief reasons for material changes.
- `compare` — `optimize` output variant: original, optimized, and concise delta. Any scores are heuristic.

## One lightweight routing decision

Determine only what changes the output: intent, complexity, critical missing context, and route.

Complexity:
- SIMPLE — localized, clear, low blast radius.
- BOUNDED — clear goal with meaningful implementation risk or several affected areas.
- COMPLEX — architectural impact, multiple independent deliverables, or unresolved product/technical decisions.

Routes: `EXECUTE_DIRECTLY`, `EXPLORE_FIRST`, `PLAN_FIRST`, `SPEC_FIRST`, `ASK_USER`.

### SIMPLE fast path

Minimally clarify scope and preservation rules. Do not build the full normalized representation. Avoid planning, headings, or tests unless they materially help the request.

### BOUNDED or COMPLEX

Inspect relevant context, then add only the useful parts of: goal, requirements, constraints, non-goals, success/Done When, and verification. Use `PLAN_FIRST` or `SPEC_FIRST` instead of immediate execution when the work is not obviously small.

For software tasks, load [references/software-engineering.md](references/software-engineering.md). For repository/project facts or BMAD artifacts, load [references/project-context.md](references/project-context.md).

## Questions

Ask only when a required fact is genuinely unknown and cannot be inferred safely from the repo or the user text. Questions are normally zero and maximum two. Prefer precise clarifying questions over broad exploration. When the request is already actionable, do not stall the work.

## Constraints

- Keep the optimized prompt brief, specific, and executable.
- Preserve user intent and required constraints; do not invent extra policy.
- Prefer the smallest useful scope, not a generalized rewrite.
- If the task is ambiguous, surface only the critical ambiguity.
- Do not execute work that should be performed by the host environment or by the user.

## Output contract

- `optimize`: final prompt only
- `audit`: readiness review only
- `explain`: final prompt plus brief reasons
- `compare`: original, optimized, and delta

## Prompt design rules

- Make the task objective explicit.
- Define acceptance criteria in concrete terms.
- Name important constraints, dependencies, and risk boundaries.
- Call out non-goals and what is intentionally out of scope.
- Keep verification steps specific and testable.
- Prefer direct instructions over background narrative.

## Examples

See [examples/examples.md](examples/examples.md) for example prompts and handoff patterns.

## Host adapters

- [adapters/opencode.md](adapters/opencode.md)
- [adapters/codex.md](adapters/codex.md)
- [adapters/claude-code.md](adapters/claude-code.md)

## Safety and quality signals

The request should be clearly scoped, bounded, and verifiable. If the task is large, prefer a `PLAN_FIRST` or `SPEC_FIRST` route. If the task is too vague, ask a narrow question instead of guessing. If critical information is missing, surface the missing fact rather than fabricating it.

## Policy reminders

- Do not execute the user request as a side effect of optimization.
- Do not add hidden requirements.
- Do not rely on BMAD or other tooling being present unless the user explicitly asks for it.
- Keep the final instruction traceable to the user intent.
- Prefer a single, concrete next step over a vague exploration plan.
- When in doubt, ask the user the smallest missing fact.

## Minimal scoring intuition

Use this only when a user asks for a heuristic judgment:

- SIMPLE: typically one focused task, normally zero or one decision point, and a narrow blast radius.
- BOUNDED: multiple steps or a small set of collaborating files; the plan is often limited and the change footprint is known.
- COMPLEX: multiple interfaces, architectural touchpoints, or uncertain dependencies; more than one significant decision or a broad verification surface.

When giving a route recommendation, prefer `EXECUTE_DIRECTLY` when the task is unambiguous and contained. Prefer `EXPLORE_FIRST`, `PLAN_FIRST`, or `SPEC_FIRST` when evidence gathering or structured planning is needed. Prefer `ASK_USER` when the missing fact changes the valid implementation path.

## Closing rule

Return the artifact the user asked for and stop. Do not continue with extra commentary or extra work unless the user explicitly asked for it.
