# Release Notes

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: release_notes
  version: 0.9.0
  rag_tags:
    - process:release
    - release:0.9.0
```

## Version 0.9.0

Release date: 2026-07-01

## Summary

The IWFM Level 4 Equivalent FM Academy is a complete, end-to-end learning programme — the full twelve-module core course, a formative and summative assessment layer, a Longleat interview-prep layer, and mobile study aids — all held to a single marking standard, and now backed by a formal product-integration schema layer and an automated repo quality check.

## Included

- Course orientation and Modules 1 to 12 (full core course).
- Module 13 Longleat Boardroom Simulation.
- Assessment layer: per-module workbook, marking guide, spoken-answer rubric, two mock exams and the final assessment.
- Interview-prep layer: 100-question interview bank (ten themed sets), 7-day crash plan, STAR answer bank and boardroom role-play prompts.
- 50-scenario FM operational scenario bank (five themed sets).
- Mobile study aids: flashcard bank, 30-day study plan and progress tracker.
- Product schemas: JSON Schema for Module, AssessmentItem, LearnerAttempt, AiTutorFeedback and LearnerProgress, with validating examples.
- Tooling: `tools/check_repo.py` for automated link, metadata and module-structure checks.
- Navigation, tags, glossary, quick start, roadmap and product-readiness pages.
- AI/RAG metadata across learning and assessment content.

## Changes Since 0.1.0

- Added Modules 9 to 12, completing the core course (0.2.0).
- Added the workbook and assessment layer (0.3.0).
- Added the 7-day crash plan and STAR answer bank (0.4.0).
- Completed the interview layer with role-play prompts and a spoken-answer rubric, and added the mobile study aids (0.5.0).
- Split the interview question bank into ten phone-sized themed sets and refreshed release documentation (0.6.0).
- Split the operational scenario bank into five phone-sized themed sets (0.7.0).
- Added the product-layer JSON schemas with validating examples (0.8.0).
- Added the automated repo quality check script and brought release notes current (0.9.0).

## Known Limitations

- The boardroom simulation remains a single file; it reads as a cohesive module and is intentionally left un-split.
- The product schemas are defined and validated in-repo but not yet implemented in FM Control Hub.
