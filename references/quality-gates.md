# Quality gates and evidence

## Gate 0 — outcome and route

Required: user/problem, desired outcome, initial boundary, constraints, success measure, open questions, and route selection.  The gate fails if the request is only a solution or technology choice with no named user outcome.

## Gate 1 — problem and evidence

Required when the work is not a bounded implementation: target user, current workflow/alternative, ranked assumptions, problem statement, evidence that affects decisions, and an explicit non-goal. The gate fails when research is a collection of links with no decision consequence.

## Gate 2 — specification

Required: scoped requirements, priority, observable acceptance criteria, named verification method, and non-functional targets with measurement. The gate fails when terms such as “easy”, “secure”, “fast”, or “ready” lack operational meaning.

## Gate 3 — plan

Required: chosen approach, material alternatives and rationale, task dependency order, links to `REQ` and `AC`, verification plan, material risks, and approval/delegation to build. The gate fails if a new agent would need to guess what to change or how to prove it.

## Gate 4 — implementation

Required for each completed slice: implementation reference, changed behavior, automated checks, observable proof, decision/deviation log, and an updated task state. The gate fails if a green build is the sole evidence of a user-visible requirement.

## Gate 5 — acceptance

Required: a matrix of every in-scope `AC`, reproducible evidence, release candidate/environment, known limitations, owner, and rollback or containment plan where relevant. The gate fails if any Must criterion is missing a disposition.

## Evidence hierarchy

Prefer evidence in this order:

1. Automated test or measurement tied directly to the criterion.
2. Reproducible browser/API/manual scenario with output, screenshot, or recording.
3. Deployed telemetry or monitored real-world behavior.
4. Explicit stakeholder acceptance with scope and date.
5. Reasoned assertion (valid only as a stated temporary risk, never as proof).

An evidence entry must say what was checked, how it was checked, where the result is stored, its result, and which `AC` it supports.

