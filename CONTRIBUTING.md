# Contributing

Contributions are welcome when they improve execution quality without turning Prompt Engineer into a large workflow framework.

## Ground rules

- Preserve the handoff-first model.
- Keep the canonical `prompt-engineer/` package at exactly seven files unless a deliberate architecture change is approved.
- Keep `SKILL.md` compact and under 500 lines.
- Keep `license: MIT` in the canonical skill frontmatter.
- Do not add host-specific behavior to the shared core when it belongs in an adapter.
- SIMPLE requests must remain lightweight.
- Inspect-before-ask and the maximum-two-question policy are part of the contract.
- Do not introduce BMAD as a runtime dependency or mutate BMAD-owned artifacts.
- Do not claim downstream improvement without real comparative execution evidence.
- If any file under `prompt-engineer/` changes after a version has been released, bump `VERSION` and add a matching `CHANGELOG.md` section before merging.

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

With GitHub CLI 2.90+ installed, run the official Agent Skills publishing validation without publishing:

```bash
gh skill publish --dry-run .
```

Scan for accidental secrets, local paths, placeholders, and stale behavior claims before committing.

## Adding or changing behavior

When behavior changes, update or add an evaluation case that describes observable expectations rather than exact optimized-prompt wording. Prefer semantic properties such as preserved scope, verification, question behavior, or routing.

## Release discipline

Versioned release assets are immutable. Never overwrite an existing `prompt-engineer-skill-vX.Y.Z.zip`. The release workflow may create a missing asset for an existing tag only when the checked-out canonical skill matches that tag. The stable `prompt-engineer-skill.zip` filename is an alias attached independently to each release, so `releases/latest/download/prompt-engineer-skill.zip` always resolves through GitHub's latest release.

Release ZIPs contain:

```text
prompt-engineer-skill.zip
├── prompt-engineer/   # exactly seven canonical skill files
└── LICENSE            # MIT license for redistribution
```

## Pull requests

Keep changes focused. Explain:

- what behavior changes;
- why it improves downstream execution or portability;
- which tests/evals cover it;
- whether the canonical seven-file package changed;
- whether `VERSION` and `CHANGELOG.md` were updated when required.
