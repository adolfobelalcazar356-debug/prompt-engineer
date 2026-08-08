# Software Engineering Reference

Load this reference only for software-development requests. The goal is to turn vague implementation intent into a bounded execution instruction without inventing architecture or business rules.

## Execution contract: use only the fields that earn their tokens

A BOUNDED/COMPLEX prompt may express:

- **Goal** — observable change or outcome.
- **Requirements** — behavior the executor can implement or demonstrate.
- **Constraints** — rules that truly restrict solution choices.
- **Non-goals** — nearby work that must remain untouched.
- **Done When** — concrete completion signal.
- **Verification** — tests, measurements, reproduction steps, or inspection that prove the result.

Do not force these into headings for SIMPLE work. Prefer natural imperative prose when that is shorter.

## By task type

### Debug

Ask the executor to inspect/reproduce before editing, distinguish evidence from assumptions, identify the **root cause**, implement the smallest correction, and add or adjust regression coverage when behavior changes. Do not prescribe the suspected cause unless the source request already establishes it.

### Refactor

State invariants before implementation: public API, observable behavior, data contracts, performance constraints, or compatibility that must remain unchanged. Use **non-goals** to prevent adjacent cleanup from expanding the patch. Reuse existing project patterns and avoid new dependencies unless need is demonstrated.

### Implement

For BOUNDED work, describe the requested behavior, relevant constraints, and how completion will be verified. For COMPLEX work with unresolved product/architecture decisions, route to PLAN_FIRST or SPEC_FIRST rather than fabricating decisions.

### Test / review

Name the behavior, boundary, or change under review. Prefer evidence from real code and real tests. Require findings to distinguish defects from suggestions. For fixes, preserve the same scope and verification rules as implementation.

### Performance

Convert "make it faster" into an evidence requirement: locate the bottleneck before optimizing and compare a relevant measurement before/after when feasible. Do not assume SQL, network, backend, frontend, or caching is the cause without evidence.

## EARS-like requirement normalization

Use **EARS** patterns only when they make behavior more observable; do not impose formal requirement syntax mechanically.

Examples:
- "works correctly" -> name the success and failure behavior that must be demonstrable.
- "improve performance" -> require evidence/measurement appropriate to the system.
- "fix the bug" -> reproduce or identify root cause, correct it, and verify regression coverage.
- "support X when Y happens" -> state the triggering condition and expected system response.

Never manufacture domain rules, thresholds, retention periods, roles, or acceptance criteria merely to fill a template.

## Scope discipline

Prefer the minimum blast radius that satisfies the goal:

- preserve unrelated behavior;
- avoid unrelated refactors;
- avoid dependency changes without demonstrated need;
- preserve public interfaces unless change is explicitly required;
- name files/components only when supplied or discoverable from the repository;
- do not claim success until verification has actually been run by the executor.

## Destructive or irreversible work

Keep destructive effects explicit. Examples include data deletion, destructive migrations, credential/security changes, destructive Git operations, broad filesystem changes, and production changes.

If scope is materially ambiguous, route to ASK_USER before producing an executable destructive instruction. If the user has made the destructive scope explicit, preserve that intent while requiring target verification, blast-radius control, and recovery/backup awareness when applicable. Never disguise an irreversible action as routine cleanup.

## Prompt compression check

Before returning the prompt, remove any sentence that does not change executor behavior. Do not repeat framework facts the executor can inspect. Do not add generic advice such as "follow best practices" unless a concrete project rule gives it meaning.
