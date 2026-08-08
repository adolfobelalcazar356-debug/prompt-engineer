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

- `optimize` â€” **default**. Return only the final prompt.
- `audit` â€” return a compact readiness review: strengths, blocking gaps, risks, and recommended route.
- `explain` â€” `optimize` output variant: final prompt plus brief reasons for material changes.
- `compare` â€” `optimize` output variant: original, optimized, and concise delta. Any scores are heuristic.

## One lightweight routing decision

Determine only what changes the output: intent, complexity, critical missing context, and route.

Complexity:
- **SIMPLE** â€” localized, clear, low blast radius.
- **BOUNDED** â€” clear goal with meaningful implementation risk or several affected areas.
- **COMPLEX** â€” architectural impact, multiple independent deliverables, or unresolved product/technical decisions.

Routes: `EXECUTE_DIRECTLy`, `EXPLORE_FIRST`, `PLAN_FIRST`, `SPEC_FIRST`, `ASK_USER`.

### SIMPLE fast path

Minimally clarify scope and preservation rules. **Do not build the full normalized representation**. Avoid planning, headings, or tests unless they materially help the request.

### BOUNDED or COMPLEX

Inspect relevant context, then add only the useful parts of: goal, requirements, constraints, **non-goals**, success/Done When, and **verification**. Use `PLAN_FIRST` or `SPEC_FIRST` instead of inventing missing decisions.

For software tasks, load [references/software-engineering.md](references/software-engineering.md). For repository/project facts or BMAD artifacts, load [references/project-context.md](references/project-context.md).

## Questions

$–ç7V7B&Vf÷&R6¶–ærâ¢¢æWfW"6²f÷"–æf÷&ÖF–öâ&VÆ–&Ç’F—66÷fW&&ÆRg&öÒF†R&W÷6—F÷'’÷"7WÆ–VB'F–f7G2à ¥VW7F–öç2&R¢¦æ÷&ÖÆÇ’¦W&ò¢¢æB¢¤Ö†–×VÒGvò¢¢â6²öæÇ’f÷"7&—F–6Âvv†W&RF–ffW&VçBç7vW'2ÖFW&–ÆÇ’6†ævR66÷RÂ6fWG’ÂFF–×7BÂ÷"F†R&WVW7FVB÷WF6öÖRâ&VfW"öæR&V6—6RVW7F–öâ÷fW"VW7F–öææ—&Rà ¢22f–æÂ&VF–æW726†V6° ¤&Vf÷&R&WGW&æ–ær$õTäDTBô4ôÕÄU‚÷WGWBÂ6öæf—&ÒF†RvöÂ—26ÆV"Væ÷Vv‚Â66÷R—2&÷VæFVBÂ7&—F–6Â6öçFW‡B—2f–Æ&ÆRÂ7V66W726â&R&V6övæ—¦VBÂfW&–f–6F–öâ—2÷76–&ÆRÂæBæò7&—F–6ÂÖ&–wV—G’&VÖ–ç2â4”ÕÄRv÷&²vWG2öæÇ’V–6²6æ—G’6†V6²à ¢22F&vWBFFW  ¤ÆöBöæÇ’F†R&VÆWfçBFFW"v†VâF†RFW7F–æF–öâ—2¶æ÷vã ¢Ò÷Vä6öFS¢¶FFW'2ö÷Væ6öFRæÖEÒ†FFW'2ö÷Væ6öFRæÖB¢Ò6öFWƒ¢¶FFW'2ö6öFW‚æÖEÒ†FFW'2ö6öFW‚æÖB¢Ò6ÆVFR6öFS¢¶FFW'2ö6ÆVFRÖ6öFRæÖEÒ†FFW'2ö6ÆVFRÖ6öFRæÖB ¤FFW'2ÖöF–g’öæÇ’†÷7B×7V6–f–26¶v–ærö–çfö6F–öâ÷"W†V7WF–öâV×†6—3²F†W’Fòæ÷B&WÆ6RF†R6÷&Rà ¢22÷WGWBF—66—Æ–æP ¤f÷"FVfVÇB÷F–Ö—¦VÂ÷WGWBöæÇ’F†Rf–æÂ&ö×C¢æòvVæW&–2&VÖ&ÆRÂ†–FFVâæÇ—6—2Â66÷&–ærÂ÷"6VÆbÖ6öæw&GVÆF–öââÖ¶R&WV—&VB&V†f–÷"F—7F–æwV—6†&ÆRg&öÒ÷F–öæÂwV–Fæ6Râ¶VWFW7G'V7F—fR÷"—'&WfW'6–&ÆRVffV7G2W‡Æ–6—B&F†W"F†â6ögFVæVBà ¤f÷"6ö×7BW†×ÆW2æB÷WGWB6†W2ÂÆöB¶W†×ÆW2öW†×ÆW2æÖEÒ†W†×ÆW2öW†×ÆW2æÖB’à