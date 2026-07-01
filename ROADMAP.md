# IWFM Level 4 FM Academy Roadmap

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: roadmap
  rag_tags:
    - roadmap:course
    - roadmap:longleat-prep
```

## Current Production Layer

Completed:

- Course orientation.
- Modules 1 to 12 (full core course).
- Module 13 Longleat Boardroom Simulation.
- 100-question Longleat interview bank.
- 50-scenario operational scenario bank.
- Navigation, glossary, tags and product-readiness pages.
- App integration plan for learner journeys, assessments, AI tutor and Longleat interview prep.

## Next Target Version

Target: `0.2.0`

The next release should prove that the academy can run as an app learning layer, not only a Markdown course.

Required v0.2.0 outcomes:

- Import modules into learner journeys.
- Create quiz and scenario assessment objects.
- Track learner progress by module, score, confidence and weak tags.
- Connect AI tutor feedback to model answers and marking guides.
- Create mobile study flow for daily lessons.
- Create Longleat interview prep mode.

## Next Modules

All twelve core modules are now complete.

## Assessment Layer

Complete:

- Workbook structure and per-module workbook questions (Modules 1 to 12).
- Model answer points and per-module marking criteria.
- Single course marking guide with bands, strands and AI-tutor rubric.
- Mock exam 1 and mock exam 2 (timed, three-section format).
- Final assessment (180-minute capstone with integrated scenario).

The next content priority is mobile-learning polish (splitting long banks, study plans, flashcards) and the product layer below.

## Product Layer

Complete:

- Formal JSON Schemas under `23-product-schemas/` for Module, AssessmentItem, LearnerAttempt, AiTutorFeedback and LearnerProgress, with worked examples that validate.
- FM Control Hub integration plan and Compliance Hub mapping (see APP_INTEGRATION_PLAN.md).
- AI tutor behaviour defined as a schema contract (AiTutorFeedback) plus the marking guide and spoken-answer rubric.

Remaining:

- Implement the schemas in FM Control Hub (import content, store attempts, serve progress).
- Mobile study flow implementation in-app.
- Split the boardroom simulation into phone-sized chunks (last long file).

## Interview Layer

Complete:

- 7-day Longleat interview crash plan (intensive, uses modules, workbook, mock exams and final assessment).
- STAR answer bank (eight Longleat themes plus five core stories and opening answers).
- Boardroom role-play prompts (six pressure scenarios with press-harder follow-ups and reader scoring).
- Spoken-answer rubric (six-dimension /24 scoring with automatic caps and AI-tutor notes).

The interview layer is now complete.

## Mobile Learning Layer

Complete:

- Flashcard bank (recall cards for all twelve modules plus cross-cutting principles, tagged to modules).
- 30-day study plan (paced four-week route through modules, workbook, mocks and final assessment).
- Progress tracker (self-assessment sheet and the progress fields for FM Control Hub).

Remaining:

- Split the boardroom simulation into phone-sized chunks. The interview bank (ten sets under `19-interview-prep/question-bank/`) and the scenario bank (five sets under `20-scenario-bank/scenarios/`) are done.
