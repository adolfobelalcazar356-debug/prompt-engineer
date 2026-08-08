# OpenCode Adapter

Use the shared core unchanged. This adapter exists only for OpenCode discovery/invocation and small execution-emphasis differences.

## Install/discovery

OpenCode stable discovers project skills from:

```text
.opencode/skills/<name>/SKILL.md
.claude/skills/<name>/SKILL.md
.agents/skills/<name>/SKILL.md
```

For a canonical package also intended for Codex, prefer copying/installing `prompt-engineer/` to:

```text
.agents/skills/prompt-engineer/
```

OpenCode exposes discovered skills through its native `skill` tool and loads the body on demand. Supporting files remain progressive; do not inline every reference into `SKILL.md`.

## Explicit MVP usage

The MVP does not depend on automatic activation. Ask OpenCode explicitly to use the `prompt-engineer` skill for the supplied request. Do not rely on V2-only autoinvoke metadata for portable behavior.

## Prompt emphasis

When OpenCode is the executor, preserve the shared prompt and emphasize only when relevant:
- inspect project instruction files and repository context before asking;
- use available tools/skills rather than restating discoverable facts;
- keep the execution prompt concise;
- verify the result before declaring completion.

Do not duplicate the core routing or software rules here.
