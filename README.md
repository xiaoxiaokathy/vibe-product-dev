# Vibe Product Dev

`vibe-product-dev` is a portable Agent Skill for turning a rough product idea into a scoped, researched, planned, implemented, and verifiably accepted increment. It is designed for Codex, Claude Code, Cursor, Copilot, and comparable coding agents that support `SKILL.md`-style instructions.

It is deliberately not a code-generation prompt. Its durable output is a traceable chain:

```text
Objective -> Requirement -> Acceptance criterion -> Task -> Evidence
```

That chain makes it possible to verify that shipped behavior solves the intended user problem rather than merely passing a convenient test suite.

## What it covers

1. Intake, scoping, constraints, and success measures.
2. User/problem discovery and assumption testing.
3. External, technical, and competitive research.
4. Product requirements and observable acceptance criteria.
5. Architecture/design decisions and an executable implementation plan.
6. Slice-by-slice implementation with evidence.
7. Acceptance, release readiness, and handoff.

The Skill selects one of three routes: `quick` for bounded work, `feature` for ordinary user-visible changes, and `product` for new/high-risk initiatives. This preserves the speed of vibe coding while adding rigor only where a decision warrants it.

## Development execution rules

All routes, including `quick`, require the same execution safeguards:

- Understand the real problem and take the shortest reliable path before editing.
- Inspect the relevant workspace, instructions, existing files, and native checks before changing anything.
- Reuse existing code and make the smallest safe local change; justify any rewrite or new abstraction.
- Write only in the active workspace and never install unrelated dependencies.
- Run proportionate existing checks and report both verified and unverified behavior.
- Before any potentially billable action, metered API enablement, paid-resource creation, quota/plan change, or new API key, disclose the service, exact action, cost, outbound data, and credential need; wait for explicit approval.

See [execution guardrails](references/execution-guardrails.md) for the decision table and confirmation format. These rules add no runtime dependency and do not automatically install packages, request credentials, create paid resources, or call external services.

## Installation

Copy the complete `vibe-product-dev/` directory into the skills directory for your agent, preserving its structure. For Codex, it can be placed under your configured Codex skills folder; for Claude Code, place or link it under `.claude/skills/` or the user skills directory. The entry point is `SKILL.md`.

Example request:

```text
Use $vibe-product-dev to turn this idea into a feature plan. Do not implement until Gate 3 is approved.
```

## Dependencies

The core Skill has no runtime package dependency. Its validation script uses only the Python standard library (Python 3.9+).

The following installed Skills are optional, but the main workflow invokes them when their trigger applies:

| Skill | When it is needed | Why it is listed |
| --- | --- | --- |
| `advise-project-approach` | Product strategy, architecture, stack/vendor choice, prioritised improvement plan, or real-world comparable research | Produces a disciplined recommendation before committing to a direction. |
| `neuroarxiv` | Non-trivial architecture, algorithm, ML/system technique, protocol, or prior-art question | Grounds technical novelty and architecture decisions in relevant arXiv work. |
| `web-access` | Any live web search, page reading, online comparative research, or browser interaction | Ensures current external claims use the approved browsing workflow. |
| `webapp-testing` | Browser-based acceptance proof for a local web app | Captures reproducible user-facing validation. |

If an optional Skill is not available, continue with the main workflow, say which evidence could not be obtained, and never present an unsupported assumption as research.

For maintainers only, the installed `skill-creator` Skill is recommended to validate the package structure after changes. Its validator currently requires the Python package `PyYAML`; that dependency is not required to use `vibe-product-dev` itself.

## Repository outputs

When a repository has no preferred process, the Skill creates one folder per change:

```text
docs/product-work/2026-08-27-export-reports/
  00-brief.md
  01-discovery.md          # only when needed
  02-research.md           # only when needed
  03-spec.md
  04-design.md
  05-plan.md
  06-acceptance-report.md
```

The files are intentionally normal Markdown so they remain reviewable in Git and usable by any agent. Template source lives in `templates/` and should not be modified per change.

## Quality model

Each phase has a gate. Gates are review points, not bureaucratic pauses: an agent may proceed when the gate’s evidence exists or when the user explicitly accepts the named risk.

| Gate | Proves |
| --- | --- |
| 0 — outcome | The smallest useful outcome, boundary, and route are understood. |
| 1 — problem | User problem, key assumptions, and decision-relevant research are clear. |
| 2 — spec | Must requirements have observable, testable acceptance criteria. |
| 3 — plan | Design decisions, tasks, verification, and ownership are sufficient to build. |
| 4 — implementation | Every slice has been validated and deviations were recorded. |
| 5 — acceptance | Every Must criterion has passing evidence, an approved waiver, or a visible open state. |

## Validate traceability

Run after spec, plan, and acceptance artifacts exist, substituting the installed Skill directory:

```powershell
python <path-to-vibe-product-dev>\scripts\check_traceability.py docs\product-work\2026-08-27-export-reports
```

The checker finds missing links and is deliberately conservative. It does not certify product quality; a human still needs to review the evidence and decide whether waivers are acceptable.

## Design principles

- Use a spec as living context, not an immutable contract.
- Keep product facts, assumptions, decisions, and research evidence distinct.
- Prefer vertical slices that show a real user outcome.
- Test the observable promise, including failure paths.
- Record material decisions near the work so a future agent is not forced to rediscover intent.
- Leave a handoff that explains limitations and operational ownership as clearly as it explains the implementation.

## Inspiration and differentiation

The design learns from [GitHub Spec Kit](https://github.com/alfasin/agentic-sdlc-spec-kit) (project principles and phase verification), [OpenSpec](https://github.com/Fission-AI/OpenSpec/) (explicit, brownfield-safe changes), [SteveVitali/agent-skills](https://github.com/SteveVitali/agent-skills) (repository-native checks and evidence-first completion), [SuperSpec](https://github.com/lbk-open/super-spec) (complexity triage and human gates), and [carlitose/agent-skills](https://github.com/carlitose/agent-skills) (explicit authority for publishing and provider actions). It differs by making product discovery, research provenance, risk-calibrated workflow choice, execution guardrails, and acceptance evidence first-class without requiring multi-agent orchestration or PR automation.

## License

No reuse license has been selected yet. Public visibility alone does not grant permission to reuse the contents. Add a `LICENSE` file before inviting external contribution or reuse; `MIT` is one suitable option for a broadly reusable workflow, subject to retaining attribution for any borrowed template content.
