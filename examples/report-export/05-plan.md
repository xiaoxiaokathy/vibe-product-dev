# Executable plan — scheduled report export

Status: Approved  
Linked spec: `03-spec.md`

## Task plan

| ID | Slice and intent | Links | Dependencies | Proof | Status |
| --- | --- | --- | --- | --- | --- |
| TASK-01 | Add a query that returns only reconciled payments for a business date. | REQ-01, AC-01 |  | Seed records in every state and run integration test. | Complete |
| TASK-02 | Generate and privately store the daily CSV. | REQ-01, REQ-02, AC-01, AC-02 | TASK-01 | Integration test asserts object path, columns, and one generated object. | Complete |
| TASK-03 | Surface run state and retry failure to operations. | REQ-03, AC-03 | TASK-02 | Browser scenario: failed run shows reason then succeeds after retry. | Complete |

