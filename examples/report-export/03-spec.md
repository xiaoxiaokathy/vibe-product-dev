# Product specification — scheduled report export

Status: Approved  
Linked brief: `00-brief.md`

## Product promise and journey

A finance operations analyst can retrieve a complete daily reconciled-payment CSV without preparing it manually.

1. At 08:45 local time the service starts a business-day export.
2. The service reads reconciled payments for the preceding business day and writes a CSV to the approved storage location.
3. Operations sees a completed or failed run with a link or a retry instruction.

## Scope

| Priority | Requirement | Acceptance criteria | Verification method |
| --- | --- | --- | --- |
| Must | REQ-01 — Generate one export for the preceding business day. | AC-01 — WHEN the scheduled run starts on a business day, THE SYSTEM SHALL create exactly one CSV containing all and only payments in reconciled state for the preceding business day. | seeded integration test |
| Must | REQ-02 — Keep payment data private. | AC-02 — WHEN an export is written, THE SYSTEM SHALL store it only in the approved private location and omit card data. | storage-policy test and column assertion |
| Must | REQ-03 — Make failures actionable. | AC-03 — WHEN an export run fails, THE SYSTEM SHALL record the failure reason and expose a retry action to operations. | browser scenario |

## Non-functional requirements

| ID | Requirement | Target | Measurement method | Rationale |
| --- | --- | --- | --- | --- |
| NFR-01 | Completion time | 95% of daily exports finish within 10 minutes after start. | job duration metric over 20 business-day runs | Analysts need the file by 09:00. |

