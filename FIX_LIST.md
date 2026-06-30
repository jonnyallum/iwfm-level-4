# Fix List

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: fix_list
  version: 0.1.0
  rag_tags:
    - process:quality-audit
    - process:release-readiness
```

## Fixed in 0.1.0

- Added missing AI/RAG metadata to early course modules.
- Corrected README repository map to include `19-interview-prep` and `20-scenario-bank`.
- Added `QUALITY_AUDIT.md`, `FIX_LIST.md`, `RELEASE_NOTES.md` and `VERSION`.

## Fixed in 0.2.0

- Built Modules 9 to 12 (Budgeting and Finance, Leadership and Communication, Strategic FM, Estate Management), completing the twelve-module core course.

## Remaining Fixes

| Priority | Item | Reason |
|---|---|---|
| High | Build workbook and assessment layers | Current learning content has scenarios and model answers, but no full workbook or final assessment. |
| Medium | Split long practice banks into mobile-first chunks | Current bank files are comprehensive but long for phone reading. |
| Medium | Add 7-day Longleat crash plan as a standalone file | Quick Start includes a path, but TODO still calls for a dedicated crash plan. |
| Low | Add automated link/metadata check script | Current audit used manual PowerShell checks. |

## Intentionally Not Fixed in This Pass

- Long files were not split because the user requested not to rewrite everything.
- Future modules and assessment items were not marked complete without production files.
- Course content was not rewritten where it already met practical FM learning needs.
