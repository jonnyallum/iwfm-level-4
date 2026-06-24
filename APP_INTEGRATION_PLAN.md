# App Integration Plan

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: app_integration_plan
  next_target_version: 0.2.0
  rag_tags:
    - product:fm-control-hub
    - product:learning-pathway
    - product:ai-tutor
    - release:0.2.0-target
```

## Plain English Summary

This plan defines how the IWFM Level 4 FM Academy should become a structured app learning layer for v0.2.0.

The repo should power learner journeys, mobile study, quizzes, scenario assessment, AI tutor feedback and Longleat interview preparation.

## Modules to Learner Journeys

| Content | Learner journey | Product use |
|---|---|---|
| Course orientation | Onboarding | Explain course purpose, expectations and study method |
| Module 1: FM Principles | Foundation | Teach FM role, service mindset and operational context |
| Module 2: Risk Management | Core skill | Teach risk language, prioritisation and evidence |
| Module 3: Health & Safety Management | Compliance foundation | Teach legal control, escalation and incident thinking |
| Module 4: Fire Safety | Life-safety pathway | Teach fire systems, doors, escape routes and action tracking |
| Module 5: Water Hygiene | Specialist compliance pathway | Teach Legionella governance and evidence |
| Module 6: Building Systems | Technical FM pathway | Teach critical systems, failure impact and handover |
| Module 7: Asset Management | Lifecycle and budget pathway | Teach asset data, backlog and capital prioritisation |
| Module 8: Contractor Management | Contractor control pathway | Teach approval, RAMS, permits and monitoring |
| Module 13: Longleat Boardroom Simulation | Capstone | Test board-level judgement under multiple incidents |
| Interview question bank | Interview prep mode | Generate practice, model points and confidence scoring |
| Scenario bank | Assessment and AI tutor mode | Present practical incidents and mark responses |

## Quiz and Assessment Schema

Recommended tables or objects:

- `learning_modules`
- `lessons`
- `quiz_questions`
- `scenario_questions`
- `model_answers`
- `marking_criteria`
- `learner_attempts`
- `ai_tutor_feedback`
- `learner_progress`

Recommended `quiz_questions` fields:

- `id`
- `module_id`
- `question_type`: multiple_choice, short_answer, scenario, hard_question, interview_prompt
- `prompt`
- `options`
- `correct_answer`
- `model_answer`
- `marking_points`
- `difficulty`
- `rag_tags`
- `compliance_bible_links`

Recommended `learner_attempts` fields:

- `id`
- `learner_id`
- `question_id`
- `submitted_answer`
- `score`
- `strengths`
- `improvements`
- `ai_feedback`
- `attempted_at`

## Progress Tracking Fields

Recommended `learner_progress` fields:

- `learner_id`
- `module_id`
- `lesson_status`
- `completion_percentage`
- `last_opened_at`
- `confidence_rating`
- `quiz_score`
- `scenario_score`
- `interview_readiness_score`
- `weak_tags`
- `strong_tags`
- `next_recommended_lesson`
- `revision_due_at`

Progress should track demonstrated understanding, not only page views.

## AI Tutor Behaviour

The AI tutor should:

- ask one question at a time;
- mark against the model answer and marking guide;
- give direct, practical feedback;
- ask the learner to improve weak answers;
- link feedback to relevant Compliance Bible sections;
- reward evidence, ownership, escalation and review;
- challenge vague answers such as "I would look into it";
- avoid pretending this is an official IWFM qualification;
- adapt difficulty based on repeated weak tags.

AI tutor prompt:

> You are an FM Level 4-style tutor. Mark the learner's answer against the module model answer and marking guide. Be direct and practical. Identify missing risk, evidence, ownership, escalation, compliance and Longleat visitor-attraction context. Give a better answer the learner can practise aloud.

## Mobile Study Flow

Recommended flow:

1. Open daily lesson.
2. Read one phone lesson.
3. Answer one quick check question.
4. Practise one scenario.
5. Review model answer.
6. Save confidence rating.
7. Get next recommended action.

Mobile rules:

- keep each screen to one concept;
- avoid long scrolling where possible;
- split large banks into filtered practice sets;
- use progress chips for modules and tags;
- provide "practise aloud" mode for interview prompts;
- allow offline reading for core modules.

## Longleat Interview Prep Mode

Longleat mode should include:

- 7-day crash pathway;
- boardroom simulation;
- 100-question interview bank;
- 50 operational scenarios;
- STAR answer builder;
- timed spoken-answer practice;
- visitor, animal, heritage and estate prompts;
- board-level escalation prompts;
- confidence score by topic.

Recommended Longleat readiness categories:

- visitor safety;
- animal welfare interfaces;
- fire and life safety;
- water hygiene;
- asbestos and contractor control;
- electrical and critical systems;
- asset backlog and budget;
- board communication.

## Minimum Viable Integration for v0.2.0

The v0.2.0 integration should deliver:

- module list and lesson navigation in-app;
- progress records for modules 1 to 8 and Module 13;
- question objects created from scenario and hard-question sections;
- scenario bank imported as scenario assessment prompts;
- interview bank imported as Longleat prep prompts;
- AI tutor feedback using model answers and marking guides;
- Compliance Bible links attached to modules;
- mobile daily lesson flow;
- Longleat interview prep mode with filtered categories;
- dashboard showing completion, weak areas and interview readiness.

## Out of Scope for v0.2.0

- Full official qualification assessment.
- Payment, cohort management or tutor admin.
- Full workbook export.
- Speech-to-text scoring beyond manual answer entry.
- Complete Modules 9 to 12 unless separately prioritised.
