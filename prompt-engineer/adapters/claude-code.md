# Claude Code Adapter

Use the shared core unchanged. This adapter covers Claude Code discovery/invocation and target-specific emphasis.

## Install/discovery

Install a project skill at:

```text
.claude/skills/prompt-engineer/SKILL.md
```

with the rest of the canonical `prompt-engineer/` directory beside it. Personal skills may live under `~/.claude/skills/`.

## Explicit MVP usage

Invoke directly with:

```text
/prompt-engineer
```

The MVP does not depend on automatic invocation. Claude Code supports a host-specific `disable-model-invocation: true` frontmatter field for manual-only skills, but do not add Claude-only frontmatter to the canonical `SKILL.md`; add it only in a Claude-specific packaged variant if strict enforcement is required.

## Prompt emphasis

When Claude Code is the executor, emphasize only when relevant:
- use `CLAUDE.md` / `AGENTS.md` and project skills as context;
- use subagents only when the task benefits from decomposition;
- use plan-first behavior only when complexity justifies it;
- preserve the handoff boundary unless the user separately asks Claude to execute the optimized prompt.

Do not duplicate shared routing or software rules here.
