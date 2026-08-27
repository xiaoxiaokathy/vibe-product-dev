# Development execution guardrails

Read this reference before implementing, changing dependencies, using an external service, or completing handoff. The rules in `SKILL.md` are mandatory; this reference explains how to apply them without adding unnecessary ceremony.

## Decide the shortest reliable path

State the problem and observable user outcome before selecting a solution. Prefer the smallest vertical change that can prove the outcome. A shortcut is not reliable if it guesses repository structure, bypasses an existing contract, omits a required validation, or creates unrecoverable external state.

## Inspect before modifying

Before a write, inspect the relevant source, nearby tests, project instructions, manifests, and existing verification configuration. Use repository evidence to discover paths and commands. If the workspace contains a suitable component, utility, convention, or test harness, reuse it unless a recorded constraint makes it unsuitable.

## Minimal-change decision table

| Situation | Required action |
| --- | --- |
| Existing file/component supports the behavior | Modify it locally and preserve unrelated behavior. |
| Existing implementation is unclear | Inspect its callers, tests, and documentation before proposing a replacement. |
| New abstraction or rewrite is needed | Explain the concrete limitation, alternatives considered, affected acceptance criteria, and rollback impact. |
| Dependency is already present | Use it only when it fits existing conventions and task scope. |
| New dependency is needed to meet an approved requirement | Record purpose, maintenance/security impact, and validation; do not install unrelated tooling. |

## Cost and credential gate

Stop before any action that may create or increase a charge, create a paid resource, enable metered usage, change a subscription/quota, or require a new API key. This gate applies even when a provider advertises a free tier, because usage, account configuration, or data egress may still create cost.

Present this compact confirmation request:

```text
Approval required
Service: <provider/product>
Action: <exact action to take>
Cost: <known pricing or "not yet verified">
Data leaving workspace: <data or "none">
Credential: <new API key / existing credential / none>
Please confirm this exact action.
```

Do not request, reveal, paste, or create credentials before approval. Existing dependencies used within their already approved configuration do not trigger this gate. A new paid capability, metered endpoint, plan/quota change, or new API key does.

## Verification and handoff

Discover and run repository-native checks proportionate to the changed surface: focused tests first, then the relevant broader check when practical. Do not claim an unrun check passed. Record each verification item with command or scenario, result, and linked acceptance criteria. Record unrun checks with a concrete reason such as unavailable environment, missing credential, blocked external service, or time explicitly accepted by the user.

The final handoff must state:

- changed behavior and linked acceptance criteria;
- checks and observable scenarios that passed;
- checks not run, their reason, and resulting risk;
- dependency changes and any approved external-service/cost action;
- remaining limitations, rollback/containment, and owner when relevant.

