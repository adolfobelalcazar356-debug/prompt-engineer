# Prompt Engineer

Portable Agent Skill for turning user intent into compact, bounded, and verifiable instructions for AI agents.

Prompt Engineer is designed for **OpenAI Codex**, **OpenCode**, and **Claude Code**. It specializes in software-engineering work while remaining useful for general research, analysis, and writing prompts.

## What it does

Prompt Engineer does more than rewrite wording. It can:

- preserve the user's original intent while removing prompt bloat;
- distinguish SIMPLE, BOUNDED, and COMPLEX work;
- inspect repository context before asking discoverable questions;
- add constraints, non-goals, completion criteria, and verification only when they materially help;
- route work to direct execution, exploration, planning, specification, or a critical user question;
- keep destructive or irreversible effects explicit;
- adapt the handoff prompt for Codex, OpenCode, or Claude Code;
- reuse relevant BMAD artifacts when present without depending on BMAD.

The default behavior is **handoff-first**: the skill produces the optimized prompt and stops. The target agent executes that prompt only when the user separately asks it to do so.

## Repository layout

```text
.
├── prompt-engineer/                 # Canonical installable skill: exactly 7 files
│   ├── SKILL.md
│   ├── adapters/
│   │   ├── claude-code.md
│   │   ├── codex.md
│   │   └── opencode.md
│   ├── examples/
│   │   └── examples.md
│   └── references/
│       ├── project-context.md
│       └── software-engineering.md
├── evals/                           # Downstream evaluation cases/runbook
├── tests/                           # Static contract tests
├── docs/ARCHITECTURE.md
├── ACKNOWLEDGMENTS.md
├── CONTRIBUTING.md
└── LICENSE
```

## Installation

### Codex

Codex loads repository skills from `.agents/skills` and personal skills from `~/.agents/skills`.

**Project-scoped:**

```bash
mkdir -p .agents/skills
cp -R prompt-engineer .agents/skills/prompt-engineer
```

**Personal:**

```bash
mkdir -p ~/.agents/skills
cp -R prompt-engineer ~/.agents/skills/prompt-engineer
```

In Codex CLI or the IDE extension, invoke explicitly with:

```text
$prompt-engineer
```

or open the skill picker with:

```text
/skills
```

Official reference: https://developers.openai.com/codex/build-skills

### OpenCode

OpenCode v2 natively discovers project skills under `.opencode/skills` and also supports `.agents/skills` and `.claude/skills` as compatibility locations. For a single install that also works with Codex, `.agents/skills` is a good portable choice.

```bash
mkdir -p .agents/skills
cp -R prompt-engineer .agents/skills/prompt-engineer
```

For a native OpenCode-only project install:

```bash
mkdir -p .opencode/skills
cp -R prompt-engineer .opencode/skills/prompt-engineer
```

Then ask OpenCode explicitly to use the `prompt-engineer` skill for the request you want optimized.

Official reference: https://opencode.ai/v2/docs/skills

### Claude Code

Claude Code loads project skills from `.claude/skills` and personal skills from `~/.claude/skills`.

```bash
mkdir -p .claude/skills
cp -R prompt-engineer .claude/skills/prompt-engineer
```

Invoke it with:

```text
/prompt-engineer
```

Official reference: https://code.claude.com/docs/en/skills

### Windows PowerShell example

From the root of this repository, to install Prompt Engineer globally for Codex:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\prompt-engineer" "$HOME\.agents\skills\prompt-engineer"
```

For Claude Code:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\prompt-engineer" "$HOME\.claude\skills\prompt-engineer"
```

## Usage

### Default: optimize

```text
$prompt-engineer
I have two existing Git repositories, a React frontend and a FastAPI backend.
I want to combine them into one repository while preserving both Git histories.
Give the target agent a safe, verifiable instruction.
```

The skill returns the optimized handoff prompt only.

### Audit

Ask Prompt Engineer to audit a request when you want a compact readiness review: strengths, blocking gaps, risk, and recommended route.

### Explain

Use `explain` when you want the optimized prompt plus a short explanation of the meaningful changes.

### Compare

Use `compare` to see the original prompt, optimized prompt, and a concise delta. Any prompt-quality score should be treated as heuristic; downstream execution quality matters more.

## Design principles

1. The best prompt is the shortest instruction that still preserves what correct execution requires.
2. Inspect before asking.
3. SIMPLE work should stay simple.
4. Do not invent architecture, business rules, thresholds, or acceptance criteria.
5. Use non-goals and verification when they reduce real execution risk.
6. Keep destructive actions explicit.
7. Measure value through downstream execution, not prompt aesthetics alone.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the current architecture.

## Verification

The repository's contract tests use only the Python standard library:

```bash
python -m unittest discover -s tests -v
```

The first downstream evaluation set contains six pressure cases: simple, debug, refactor-scope, complex, ambiguous-destructive, and explicit-destructive work. See [evals/README.md](evals/README.md).

## Status

**MVP / early public release.** Static contract verification is included. Claims that Prompt Engineer improves downstream execution should be based on actual comparative runs, not inferred from the prompt text alone.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgments and trademarks

See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for conceptual influences and third-party projects. Product and project names belong to their respective owners. This project is independent and is not endorsed by OpenAI, Anthropic, OpenCode, or BMad Code.
