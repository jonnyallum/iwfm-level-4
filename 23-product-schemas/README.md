# Product Schemas

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: product_schema_index
  rag_tags:
    - product:fm-control-hub
    - product:schema
    - integration:learning-layer
```

## Purpose

These JSON Schemas turn the academy content into a machine-readable learning layer for FM Control Hub. They formalise the objects sketched in prose in the [app integration plan](../APP_INTEGRATION_PLAN.md) and the fields in the [progress tracker](../22-study-plans/progress-tracker.md), so content, attempts, marking and progress can be imported, stored and served consistently.

All schemas are JSON Schema draft 2020-12 and validate independently. See [examples.md](examples.md) for worked instances.

## Entity Map

```text
Module ─────────────┐
  (course content)  │  owns
                    ▼
             AssessmentItem ──────── answered by ──────► LearnerAttempt
   (workbook / quiz / scenario /                          (one answer +
    interview / flashcard /                                mark + feedback)
    mock / final questions)                                     │
                                                                │ marked by
                                                                ▼
                                                        AiTutorFeedback
                    ┌───────────────────────────────────────────┘
                    ▼  rolls up into
             LearnerProgress
   (per-module status, bands, weak tags, readiness)
```

## Schemas

| Schema | File | Represents |
|---|---|---|
| Module | [module.schema.json](module.schema.json) | A course module or capstone, mapped to its learner journey and content files. |
| AssessmentItem | [assessment-item.schema.json](assessment-item.schema.json) | Any question-like object: workbook, quiz, scenario, hard question, interview prompt, flashcard, mock or final question. |
| LearnerAttempt | [learner-attempt.schema.json](learner-attempt.schema.json) | One learner answer with band, marks and (for spoken practice) the /24 rubric. |
| AiTutorFeedback | [ai-tutor-feedback.schema.json](ai-tutor-feedback.schema.json) | Structured tutor marking output: band, reason, strongest moment, fix, missing elements. |
| LearnerProgress | [learner-progress.schema.json](learner-progress.schema.json) | Per-module progress, weak/strong tags and derived readiness. |

## How These Map to the Academy

- **Modules 1-13** → `Module` records (`content_path` points at the module markdown; `workbook_path` at its workbook).
- **Workbook, mock exams, final assessment, themed question sets, scenario sets, flashcards** → `AssessmentItem` records (the `item_type` and `theme` enums cover every source).
- **Marking guide bands** (`Distinction`/`Pass`/`Borderline`/`Not yet`) and **spoken rubric** (six dimensions, /24, `Interview-ready`…`Not yet`) → `LearnerAttempt` and `AiTutorFeedback`.
- **Automatic caps** (trading safety, bluffing, reliance on reputation, no decision) → `capped_reason` / `cap_applied`.
- **Progress tracker fields and readiness checklist** → `LearnerProgress`.

## AI Tutor Contract

The AI tutor consumes an `AssessmentItem` (with `model_answer` and `marking_points`) plus a `LearnerAttempt.submitted_answer`, and must emit an `AiTutorFeedback` object. This makes the tutor behaviour in the [app integration plan](../APP_INTEGRATION_PLAN.md) and the [marking guide](../17-marking-guides/marking-guide.md) enforceable by schema rather than prose.

## Validation

Each `*.schema.json` is self-contained. Validate an instance against a schema with any draft-2020-12 validator, for example:

```bash
# using ajv-cli
ajv validate -s assessment-item.schema.json -d my-item.json
```

## Related

- [App integration plan](../APP_INTEGRATION_PLAN.md)
- [Progress tracker](../22-study-plans/progress-tracker.md)
- [Marking guide](../17-marking-guides/marking-guide.md)
- [Spoken-answer rubric](../17-marking-guides/spoken-answer-rubric.md)
- [How to use this in FM Control Hub](../HOW_TO_USE_IN_FM_CONTROL_HUB.md)
- [Master index](../MASTER_INDEX.md)
