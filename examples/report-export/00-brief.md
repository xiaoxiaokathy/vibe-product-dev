# Brief — scheduled report export

Status: Approved  
Route: feature  
Owner: Product lead  
Last updated: 2026-08-27

## Problem and outcome

- **OBJ-01 — Outcome:** A finance operations analyst can receive a CSV of the previous day's reconciled payments by 09:00 local time without manual spreadsheet work.
- **Problem:** Analysts manually filter and export payments every morning, creating delays and transcription risk.
- **Why now:** The team will add two regional payment channels next quarter.
- **Success signal:** In the first month, 90% of business-day exports complete before 09:00 and no manual export is required.

## Scope

- In scope: scheduled daily CSV export, delivery to approved object storage, run status visible to operations.
- Out of scope: custom report builder, historical backfill UI, arbitrary external email delivery.
- Constraints: reuse current payments read model; no payment card data in export; retain export logs for 90 days.

## Context and uncertainty

| ID | Type | Statement | Impact if wrong | Owner / resolution |
| --- | --- | --- | --- | --- |
| ASM-01 | Assumption | Reconciled state is final by 08:30 on business days. | High | Confirm with payments owner before Gate 2. |

## Gate 0 decision

- Route rationale: User-visible recurring workflow with data/privacy constraints.
- Approval/delegation to continue: Approved for research and specification.
- Next artifact: `02-research.md`.

