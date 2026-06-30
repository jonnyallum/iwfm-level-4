# Learner Progress Tracker

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: progress_tracker
  rag_tags:
    - study:progress-tracker
    - workflow:self-assessment
    - product:fm-control-hub
```

## Purpose

A simple self-tracking sheet so a learner can see, in one place, what they have studied, how they scored, and which tags are still weak. Copy this file, fill it in as you go, and let the **weak tags** column drive your revision. It also defines the fields the [FM Control Hub](../HOW_TO_USE_IN_FM_CONTROL_HUB.md) progress layer can store per learner.

> Be honest. A green row you can't actually defend out loud is not green. Mark to the standard in the [marking guide](../17-marking-guides/marking-guide.md).

## How to Score Each Row

- **Status:** Not started / Reading / Practised / Confident.
- **Workbook band:** Distinction / Pass / Borderline / Not yet (from the [marking guide](../17-marking-guides/marking-guide.md)).
- **Confidence:** 1 (shaky) to 5 (could teach it).
- **Weak tags:** note the specific gap so revision is targeted, not vague.

## Module Progress

| Module | Status | Workbook band | Confidence 1-5 | Weak tags / notes |
|---|---|---|---|---|
| 1 FM Principles | | | | |
| 2 Risk Management | | | | |
| 3 Health & Safety | | | | |
| 4 Fire Safety | | | | |
| 5 Water Hygiene | | | | |
| 6 Building Systems | | | | |
| 7 Asset Management | | | | |
| 8 Contractor Management | | | | |
| 9 Budgeting & Finance | | | | |
| 10 Leadership & Communication | | | | |
| 11 Strategic FM | | | | |
| 12 Estate Management | | | | |
| 13 Boardroom Simulation | | | | |

## Assessment Results

| Assessment | Date | Score | Band | Weakest areas |
|---|---|---|---|---|
| Mock Exam 1 | | / 100 | | |
| Mock Exam 2 | | / 100 | | |
| Final Assessment | | / 100 | | |

## Interview Practice

| Item | Date | Spoken rubric /24 | Band | Note |
|---|---|---|---|---|
| Interview bank (first 40) | | | | |
| Role-play session 1 | | | | |
| Role-play session 2 | | | | |
| Five STAR stories rehearsed | | | | |

## Weak-Tag Watchlist

List the tags you keep scoring low on. Revisit the matching module and re-drill its flashcards until the tag clears.

| Weak tag | Module to revisit | Cleared? |
|---|---|---|
| | | |
| | | |
| | | |

## Readiness Checklist

- [ ] All 12 modules at Confident.
- [ ] All workbooks at Pass or better.
- [ ] Both mock exams at Pass or better.
- [ ] Final assessment at Pass or better.
- [ ] Five STAR stories rehearsed out loud.
- [ ] Held a safety-first decision under role-play pressure.
- [ ] Weak-tag watchlist cleared.

When every box is ticked, you are ready for a Longleat-style operational FM interview.

## Suggested Progress Fields (for FM Control Hub)

For the product integration, each learner record can store:

- `learner_id`, `module_id`, `status`, `workbook_band`, `confidence_score`, `weak_tags[]`;
- `assessment_id`, `score`, `band`, `attempt_date`;
- `spoken_rubric_score`, `roleplay_band`;
- `readiness_flag` (derived when the readiness checklist is fully met).

## Related

- [30-day study plan](30-day-study-plan.md)
- [Marking guide](../17-marking-guides/marking-guide.md)
- [Spoken-answer rubric](../17-marking-guides/spoken-answer-rubric.md)
- [How to use this in FM Control Hub](../HOW_TO_USE_IN_FM_CONTROL_HUB.md)
- [Master index](../MASTER_INDEX.md)
