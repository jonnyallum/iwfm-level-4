# Quality Audit

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: quality_audit
  version: 0.1.0
  audit_date: 2026-06-24
  rag_tags:
    - process:quality-audit
    - release:0.1.0
```

## Audit Scope

This audit checked the repository for:

- duplicate content;
- weak generic sections;
- missing official sources where relevant;
- broken internal links;
- inconsistent naming;
- TODO items marked complete without matching files;
- schema/table mismatches;
- missing AI/RAG metadata;
- files that are too long for mobile reading;
- Longleat content that is too generic.

## Summary

The repo is suitable for a `0.1.0` learning-content release after this fix pass. The main clear defects were missing AI/RAG metadata in early modules and README repository map drift after the interview and scenario banks were added. Both have been fixed.

## Findings

| Area | Result | Notes |
|---|---|---|
| Duplicate content | Pass | No material duplicate modules or banks found. Repeated answer structure is intentional for learning consistency. |
| Weak generic sections | Pass | Modules use practical FM scenarios, model answers and marking criteria. |
| Missing official sources | Not applicable | This repo is the learning layer; legal sources are linked through Compliance Bible. |
| Broken internal links | Pass | Link check found no broken internal Markdown links. |
| Inconsistent naming | Fixed | README map updated to include `19-interview-prep` and `20-scenario-bank`. |
| TODO completion evidence | Pass with note | Interview answer bank is represented by the 100-question bank with expected answer points. |
| Schema/table mismatches | Not applicable | No database schema lives in this repo. |
| Missing AI/RAG metadata | Fixed | Metadata blocks added to modules that were missing them. |
| Mobile reading length | Risk accepted | The interview bank, scenario bank and boardroom simulation are long but intentionally comprehensive. |
| Longleat relevance | Pass | Longleat content includes visitor numbers, board pressure, animal infrastructure, power outage, asbestos and water hygiene scenarios. |

## Long Files

These files should be split in a later mobile-polish pass:

- `19-interview-prep/longleat-interview-question-bank.md`
- `13-longleat-simulation/longleat-boardroom-simulation.md`
- `20-scenario-bank/fm-operational-scenario-bank.md`

## Fixes Applied

- Added missing AI/RAG metadata blocks to course modules.
- Corrected README repository map to include interview and scenario bank folders.
- Added release and audit artefacts.

## Residual Risks

- Modules 9 to 12 remain intentionally incomplete.
- Workbook, assessment, mock exam and product mapping layers remain intentionally incomplete.
- Large practice banks are not ideal for phone-first reading until split into smaller files.
