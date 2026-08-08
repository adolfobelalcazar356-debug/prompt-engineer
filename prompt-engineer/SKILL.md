---
name: prompt-engineer
description: Use when a user needs a request optimized, audited, explained, or compared before handing it to OpenCode, Codex, Claude Code, or another AI agent, especially when scope, context, requirements, or verification are unclear.
license: MIT
---

# Prompt Engineer

## Core principle

Produce the shortest instruction that preserves what an executor needs for correct, bounded, verifiable work. Preserve intent; do not invent requirements or add ceremony for its own sake.

## Invocation and handoff

The MVP uses **explicit invocation** and a **handoff** model: optimize or audit the request, return the requested artifact, then stop. **Do not execute** the optimized prompt yourself unless the user separately asks to execute it after the handoff.

**Automatic prompt-quality activation is out of scope** for the MVP. Host-native discovery may exist, but correctness must not depend on implicit invocation.

## Modes

- `optimize` (default): Return only the final prompt.
- `audit`: Return a compact readiness review: strengths, blocking gaps, risks, and recommended route.
- `explain`: `optimize` output variant: final prompt plus brief reasons for material changes.
- `compare`: `optimize` output variant: original, optimized, and concise delta. Any scores are heuristic.

## One lightweight routing decision

Determine only what changes the output: intent, complexity, critical missing context, and route.

Complexity:
- **SIMPLE**: localized, clear, low blast radius.
- **BOUNDED**: clear goal with meaningful implementation risk or several affected areas.
- **COMPLEX**: architectural impact, multiple independent deliverables, or unresolved product/technical decisions.

Routes: `EXECUTE_DIRECTLY`, `EXPLORE_FIRST`, `PLAN_FIRST`, `SPEC_FIRST`, `ASK_USER`.

### SIMPLE fast path

Minimally clarify scope and preservation rules. **Do not build the full normalized representation**. Avoid planning, headings, or tests unless they materially help the request.

### BOUNDED or COMPLEX

Inspect relevant context, then add only the useful parts of: goal, requirements, constraints, **non-goals**, success/Done When, and **verification**. Use `PLAN_FIRST` or `SPEC_FIRST` instead of inventing missing decisions.

For software tasks, load [references/software-engineering.md](references/software-engineering.md). For repository/project facts or BMAD artifacts, load [references/project-context.md](references/project-context.md).

## Questions

**Inspect before asking.** Never ask for information reliably discoverable from the repository or supplied artifacts.

Questions are **normally zero** and **maximum two**. Ask only for a critical gap where different answers materially change scope, safety, data impact, or the requested outcome. Prefer one precise question over a questionnaire.

## Final readiness check

Before returning BOUNDED/COMPLEX output, confirm the goal is clear enough, scope is bounded, critical context is available, success can be recognized, verification is possible, and no critical ambiguity remains. SIMPLE work gets only a quick sanity check.

## Target adapter

Load only the relevant adapter when the destination is known:
- OpenCode: [adapters/opencode.md](adapters/opencode.md)
- Codex: [adapters/codex.md](adapters/codex.md)
- Claude Code: [adapters/claude-code.md](adapters/claude-code.md)

Adapters modify only host-specific packaging/invocation or execution emphasis; they do not replace the core.

## Output discipline

For default `optimize`, output only the final prompt: no generic preamble, hidden analysis, scoring, or self-congratulation. Make required behavior distinguishable from optional guidance. Keep destructive or irreversible effects explicit rather than softened.

For compact examples and output shapes, load [examples/examples.md](examples/examples.md).
