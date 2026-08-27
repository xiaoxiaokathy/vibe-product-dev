---
name: vibe-product-dev
description: Guide AI-assisted product development from an ambiguous idea through research, product specification, architecture, executable planning, implementation, validation, and handoff. Use for new products, meaningful features, product discovery, implementation plans, or acceptance of vibe-coded work in Codex, Claude Code, Cursor, and similar coding agents.
---

# Vibe Product Development Loop

Turn an idea into an evidence-backed, reviewable, and verifiably accepted product increment. Treat code as one deliverable, not the deliverable. The durable source of truth is the chain:

`Objective -> Requirement -> Acceptance criterion -> Task -> Evidence`

## Mandatory development guardrails

Apply these rules on every route. `quick` reduces documentation ceremony, never safety, authorization, or verification.

1. Identify the actual problem, user outcome, and shortest reliable path before choosing research, planning, or implementation.
2. Before modifying anything, inspect the relevant workspace files, project instructions, existing structure, and repository-native validation commands. Do not guess paths, conventions, or commands.
3. Reuse the existing design and make the smallest local change that meets the acceptance criteria. Rewrite or introduce a new abstraction only when the existing structure cannot safely support the outcome; record why.
4. Write only inside the current workspace. Do not install or configure dependencies unrelated to the approved task.
5. Before an action that may incur cost, create a paid resource, enable a metered API, change a billable quota/plan, or require a new API key, disclose the service, action, known or unknown cost, data that would leave the workspace, and required credential. Stop until the user explicitly approves that exact action.
6. After implementation, run the discovered existing checks that are proportionate to the change. In the final report, separate what was verified from what was not verified and explain why.

Read `references/execution-guardrails.md` before implementation, dependency changes, external-service work, or final handoff.

## Operating contract

1. Start by identifying the current lifecycle phase. Do not recreate artifacts that are already present; inspect and improve them.
2. Select the lightest route that can safely answer the request. Do not impose full-product ceremony on a one-line fix.
3. State assumptions explicitly. Ask a narrow question only when its answer would materially change scope, cost, risk, or delivery.
4. Separate facts, user decisions, assumptions, and recommendations. Research claims need a source and a relevance note.
5. Do not write implementation code until scope, acceptance criteria, and a validation method are agreed or explicitly delegated to the user.
6. A change in requirement, architecture, or acceptance criteria invalidates affected downstream artifacts. Record the change and return to the appropriate gate.
7. Never declare a result done merely because tests pass. Close only after all in-scope acceptance criteria have evidence, an accepted exception, or an explicit defer decision.

## Select a route

Classify before producing artifacts.

| Route | Use when | Required phases |
| --- | --- | --- |
| `quick` | A bounded fix, experiment, or internal tool with one evident path | Brief -> Plan -> Build -> Verify |
| `feature` | A user-visible feature, integration, multi-file change, or uncertain solution | Brief -> Discovery/Research -> Spec -> Design/Plan -> Build -> Accept |
| `product` | A new product, major workflow, regulated domain, spend/contract decision, or multiple user roles | All phases, including staged release and operational readiness |

Escalate a route when there is an unresolved product decision, irreversible data/API decision, privacy/security risk, external dependency, or more than one plausible architecture. De-escalate only after recording why the work is low-risk and reversible.

## Workspace and artifacts

Use the repository's existing conventions first. If none exist, create a single change folder:

```text
docs/product-work/<YYYY-MM-DD>-<slug>/
  00-brief.md
  01-discovery.md
  02-research.md
  03-spec.md
  04-design.md
  05-plan.md
  06-acceptance-report.md
```

Copy only the templates needed from `templates/`. Keep implementation code, tests, and normal technical docs in their conventional locations. Link to them from the artifact rather than duplicating them.

Use stable IDs throughout: `OBJ-#`, `ASM-#`, `RSK-#`, `RES-#`, `REQ-#`, `AC-#`, `ADR-#`, `TASK-#`, `EVD-#`. Preserve IDs after edits; mark removed items as superseded.

## Phase 0 — Intake and brief

Create or update `00-brief.md` using `templates/brief.md`.

Extract:

- The user and the problem in their words.
- Desired outcome and measurable success signal.
- In-scope and deliberately out-of-scope items.
- Constraints: deadline, budget, stack, platform, data, compliance, integrations, and operating owner.
- Known context plus the questions or assumptions still open.

**Gate 0:** confirm a smallest useful outcome and a decision on the delivery route. If the goal is still vague, run discovery rather than inventing a PRD.

## Phase 1 — Discovery and research

Run discovery for unclear user/problem/market fit; run research when a decision depends on external, technical, market, UX, legal, security, or open-source facts.

Discovery must produce:

- target users and their current workflow;
- jobs, pain points, desired gains, and alternatives;
- problem statement and opportunity boundaries;
- assumptions ranked by impact and uncertainty;
- an experiment or question that can invalidate the riskiest assumption.

For research, use `templates/research.md`. Research breadth must match the decision. Prefer primary sources: official product documentation, original papers, standards, source repositories, release notes, and verified project artifacts. For every recommendation record source, date, evidence, applicability, limitations, and the resulting decision.

When research concerns a non-trivial technical architecture, algorithm, protocol, ML/system technique, or “has this been solved before?” question, invoke the `neuroarxiv` skill before settling on an architecture. When comparative product/stack strategy is needed, invoke `advise-project-approach`. For live web facts, invoke `web-access`.

**Gate 1:** a reviewer can identify the user problem, the riskiest assumptions, decision-relevant evidence, and what will not be pursued now.

## Phase 2 — Product specification

Create `03-spec.md` from `templates/spec.md`. It must include:

- a one-sentence product promise and user journey;
- requirements written as observable behavior, not implementation prescriptions;
- priorities (Must / Should / Could / Won't) and scope boundary;
- EARS-style acceptance criteria: `WHEN <trigger/context>, THE SYSTEM SHALL <observable behavior>`;
- non-functional requirements with metric, measurement method, and target;
- edge cases, failure states, accessibility, privacy/security, analytics, and support needs when applicable.

Do not use vague acceptance statements such as “fast”, “intuitive”, or “production-ready”. Convert them to an observable criterion or mark them undecided.

**Gate 2:** every Must requirement has one or more acceptance criteria, and each criterion is testable by a named method (automated test, browser scenario, manual check, metric, or stakeholder review).

## Phase 3 — Design and executable plan

Create `04-design.md` and `05-plan.md` from templates.

The design explains alternatives, selected approach, architecture boundaries, data/API contracts, user experience states, failure handling, security/privacy posture, migration/rollback, and ADRs for material decisions. It must distinguish known repository facts from proposed changes.

The plan is executable by another agent with a clean context. Break work into vertical, independently verifiable slices. For each `TASK` include:

- intent and linked `REQ`/`AC`;
- likely files or system surface, dependency order, and implementation steps;
- proof command or scenario, expected result, and rollback/containment if relevant;
- status and a stop/escalation condition.

**Gate 3:** no unowned task, no unverified Must acceptance criterion, and no material decision lacking a recorded rationale. Obtain human approval before coding if the user has not explicitly delegated that authority.

## Phase 4 — Build with controlled feedback

Implement one vertical slice at a time. Before each slice, restate linked criteria and verification. After it:

1. run proportionate automated checks;
2. perform the named observable proof;
3. update task status and evidence link;
4. record a decision, deviation, or risk if reality changed.

Stop and return to the plan if the work expands scope, changes architecture, reveals missing acceptance criteria, fails a non-trivial validation, or makes rollback materially harder. Do not silently “fix forward” a product decision.

## Phase 5 — Acceptance, release, and handoff

Create `06-acceptance-report.md` using `templates/acceptance-report.md`.

Validate actual behavior against every in-scope `AC`, including negative and degraded states. Evidence should be reproducible: command output, test identifier, screenshot, deployed URL/version, metrics query, recording, or an explicit stakeholder sign-off.

Report:

- release candidate/version and environment;
- acceptance matrix: pass, fail, blocked, waived, or deferred;
- test and manual validation results;
- known limitations, operational metrics/alerts, rollback steps, and ownership;
- scope changes and unresolved follow-ups.

Use the supplied traceability checker before presenting completion. A delivery may be called **accepted** only when every Must `AC` has passing evidence or an explicitly approved waiver. Otherwise call it **implemented with open acceptance items**.

## Communication format

At each phase report concisely:

```text
Phase: <name> | Route: <quick|feature|product>
Decision needed: <none or one precise decision>
Produced: <artifact links>
Evidence: <facts/proofs>
Next gate: <what must be true to proceed>
```

## Included resources

- `references/quality-gates.md` — complete definitions of quality gates and evidence quality.
- `references/execution-guardrails.md` — required pre-modification inspection, minimal-change, dependency, cost/API-key, and verification decisions.
- `references/research-standard.md` — research discipline and source hierarchy.
- `templates/` — change artifacts to copy and fill.
- `scripts/check_traceability.py` — checks that requirements, criteria, tasks, and evidence are connected.
