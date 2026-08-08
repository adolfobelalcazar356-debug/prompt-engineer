# Codex Adapter

Use the shared core unchanged. This adapter covers Codex discovery/invocation and target-specific emphasis.

## Install/discovery

Codex scans repository skills from `.agents/skills` from the current working directory up to the repository root. Install the canonical package at:

```text
.agents/skills/prompt-engineer/
```

User-scoped skills may live under `~/.agents/skills/`.

## Explicit MVP usage

In Codex CLI or the IDE extension, explicitly invoke with the skill mention or picker, for example:

```text
$prompt-engineer
```

or use:

```text
/skills
```

The MVP does not require implicit invocation. If a Codex deployment needs hard explicit-only policy, an optional host-specific `agents/openai.yaml` can set `policy.allow_implicit_invocation: false`; keep that file outside the seven-file canonical core unless the deployment actually needs it.

## Prompt emphasis

When Codex is the executor, emphasize only when relevant:
- precise scope and minimum necessary file changes;
- inspect-before-edit;
- tests/verification and observable completion criteria;
- no unrelated refactors or dependency changes without demonstrated need.

Do not duplicate shared routing, question, or software-engineering rules here.
