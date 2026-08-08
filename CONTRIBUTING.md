# Contributing

Contributions are welcome when they improve execution quality without turning Prompt Engineer into a large workflow framework.

## Ground rules

- Preserve the handoff-first model.
- Keep the canonical `prompt-engineer/` package at exactly seven files unless a deliberate architecture change is approved.
- Keep `SKILL.md` compact and under 500 lines.
- Do not add host-specific behavior to the shared core when it belongs in an adapter.
- SIMPLE requests must remain lightweight.
- Inspect-before-ask and the maximum-two-question policy are part of the contract.
- Do not introduce BMAD as a runtime dependency or mutate BMAD-owned artifacts.
- Do not claim downstream improvement without real comparative execution evidence.

## Before opening a pull request

Run:

```bash
python -m unittest discover -s tests -v
```

Also verify:

```bash
find prompt-engineer -type f | wc -l
```

The result should be `7`.

Scan for accidental secrets, local paths, placeholders, and stale behavior claims before committing.

## Adding or changing behavior

When behavior changes, update or add an evaluation case that describes observable expectations rather than exact optimized-prompt wording. Prefer semantic properties such as preserved scope, verification, question behavior, or routing.

## Pull requests

Keep changes focused. Explain:

- what behavior changes;
- why it improves downstream execution or portability;
- which tests/evals cover it;
- whether the canonical seven-file package changed.
