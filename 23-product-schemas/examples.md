# Product Schema Examples

```yaml
ai_metadata:
  repo: iwfm-level-4
  document_type: product_schema_examples
  rag_tags:
    - product:fm-control-hub
    - product:schema
    - integration:learning-layer
```

Worked instance examples for each schema in this folder. These are illustrative and validate against their schemas.

## Module

```json
{
  "id": "module-09",
  "number": 9,
  "title": "Budgeting and Finance",
  "slug": "budgeting-finance",
  "learner_journey": "lifecycle-budget",
  "content_path": "09-budgeting-finance/module-09-budgeting-finance.md",
  "workbook_path": "14-workbook/module-09-workbook.md",
  "learning_outcomes": [
    "explain the difference between opex and capex",
    "build and defend an FM budget",
    "explain whole-life cost instead of lowest price"
  ],
  "lesson_count": 3,
  "rag_tags": ["module:budgeting-finance", "product:fm-control-hub"],
  "compliance_bible_links": ["Statutory compliance matrix", "Asset management framework"]
}
```

## AssessmentItem — interview prompt

```json
{
  "id": "interview-q-045",
  "item_type": "interview_prompt",
  "module_id": "module-06",
  "theme": "electrical-critical-systems",
  "prompt": "How would you respond to a power outage with 5,000 visitors onsite?",
  "marking_points": [
    "life safety",
    "critical systems",
    "visitor communication",
    "generators",
    "incident log"
  ],
  "difficulty": "judgement",
  "rag_tags": ["audience:longleat-interview", "theme:electrical-critical-systems"],
  "source_path": "19-interview-prep/question-bank/05-electrical-critical-systems.md"
}
```

## AssessmentItem — flashcard

```json
{
  "id": "flash-water-01",
  "item_type": "flashcard",
  "module_id": "module-05",
  "theme": "water-hygiene",
  "prompt": "Two temperature principles that control Legionella?",
  "flip": "Keep hot water hot and cold water cold; keep water moving (flush low-use outlets).",
  "difficulty": "knowledge",
  "source_path": "21-flashcards/flashcard-bank.md"
}
```

## LearnerAttempt — spoken

```json
{
  "id": "attempt-8842",
  "learner_id": "learner-017",
  "item_id": "interview-q-045",
  "mode": "spoken",
  "submitted_answer": "First I confirm life-safety systems — emergency lighting and fire detection...",
  "band": "Pass",
  "spoken_rubric": {
    "decision": 3,
    "safety_priority": 4,
    "structure": 3,
    "composure": 3,
    "audience_language": 2,
    "brevity": 2,
    "total": 17,
    "band": "Nearly there"
  },
  "strengths": ["prioritised life-safety systems immediately"],
  "improvements": ["decide faster and close more cleanly"],
  "ai_feedback_id": "feedback-8842",
  "attempted_at": "2026-07-01T10:22:00Z"
}
```

## AiTutorFeedback

```json
{
  "id": "feedback-8842",
  "attempt_id": "attempt-8842",
  "band": "Nearly there",
  "reason": "Safe and structured but slow to decide and a little long.",
  "strongest_moment": "Confirmed life-safety systems before anything else.",
  "most_useful_fix": "State the decision in the first two sentences, then justify.",
  "missing_elements": ["review-prevention"],
  "weak_tag": "brevity",
  "cap_applied": false,
  "better_answer": "I take incident command. Life safety first: confirm emergency lighting and fire detection, then...",
  "compliance_bible_links": ["Statutory compliance matrix"],
  "generated_at": "2026-07-01T10:22:05Z"
}
```

## LearnerProgress

```json
{
  "learner_id": "learner-017",
  "module_id": "module-06",
  "lesson_status": "practised",
  "completion_percentage": 80,
  "confidence_rating": 4,
  "workbook_band": "Pass",
  "quiz_score": 72,
  "scenario_score": 68,
  "interview_readiness_score": 71,
  "weak_tags": ["brevity"],
  "strong_tags": ["fire-safety", "water-hygiene"],
  "next_recommended_lesson": "07-asset-management/module-07-asset-management.md",
  "revision_due_at": "2026-07-05T09:00:00Z",
  "last_opened_at": "2026-07-01T10:25:00Z",
  "readiness_flag": false
}
```

## Related

- [Product schemas README](README.md)
- [Master index](../MASTER_INDEX.md)
