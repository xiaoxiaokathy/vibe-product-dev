# Executable plan — scheduled report export

Status: Approved  
Linked spec: `03-spec.md`

## Pre-implementation findings and gates

- Actual problem and shortest reliable path: Generate the existing reconciled-payment view on a schedule rather than building a custom report builder.
- Files, instructions, conventions, and existing checks inspected: Payments read model, existing private-object-storage policy, job test harness, and operations run-status UI.
- Reuse/minimal-change decision: Add an export job and status view beside the existing reconciliation workflow; do not rewrite payment reconciliation.
- Dependency change: None.
- Cost/API key gate: Not applicable — approved storage and job services are already configured; no new metered capability or API key is needed.

## Task plan

| ID | Slice and intent | Links | Dependencies | Proof | Status |
| --- | --- | --- | --- | --- | --- |
| TASK-01 | Add a query that returns only reconciled payments for a business date. | REQ-01, AC-01 |  | Seed records in every state and run integration test. | Complete |
| TASK-02 | Generate and privately store the daily CSV. | REQ-01, REQ-02, AC-01, AC-02 | TASK-01 | Integration test asserts object path, columns, and one generated object. | Complete |
| TASK-03 | Surface run state and retry failure to operations. | REQ-03, AC-03 | TASK-02 | Browser scenario: failed run shows reason then succeeds after retry. | Complete |
