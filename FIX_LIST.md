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

## Fixed in 0.3.0

- Built the workbook and assessment layers: per-module workbook, marking guide, two mock exams and the final assessment.

## Fixed in 0.4.0

- Added the standalone 7-day Longleat interview crash plan and the STAR answer bank.

## Fixed in 0.5.0

- Completed the interview layer with boardroom role-play prompts and a spoken-answer rubric.
- Added the mobile study aids: flashcard bank, 30-day study plan and progress tracker.

## Remaining Fixes

| Priority | Item | Reason |
|---|---|---|
| Medium | Split long practice banks into mobile-first chunks | Current bank files are comprehensive but long for phone reading. |
| Low | Build the product layer schemas (quiz, assessment, progress) | Progress fields are sketched in the tracker; full schemas remain for FM Control Hub integration. |
| Low | Add automated link/metadata check script | Current audit used manual PowerShell checks. |

## Intentionally Not Fixed in This Pass

- Long files were not split because the user requested not to rewrite everything.
- Future modules and assessment items were not marked complete without production files.
- Course content was not rewritten where it already met practical FM learning needs.
