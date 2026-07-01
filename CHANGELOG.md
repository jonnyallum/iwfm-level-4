# Changelog

All notable changes to this repository will be recorded here.

## 2026-07-01 (repo quality tooling)

### Added

- Added `tools/check_repo.py`, an automated quality checker that verifies internal Markdown/JSON links resolve, content files carry an `ai_metadata` block, and course module files contain the required section headings. Exits non-zero for use in pre-commit, CI or SessionStart hooks.
- Added `tools/README.md` documenting the checker and how to extend it.

### Changed

- Added an `ai_metadata` block to `RELEASE_NOTES.md` and brought it current to version 0.9.0 (it had drifted).
- Referenced the checker in CONTRIBUTING.md and COMMIT_GUIDE.md.
- Updated FIX_LIST.md (the automated check script item is now done).
- Bumped VERSION to 0.9.0.

## 2026-07-01 (product schemas)

### Added

- Added `23-product-schemas/` with formal JSON Schema (draft 2020-12) files for the FM Control Hub learning layer: `module.schema.json`, `assessment-item.schema.json`, `learner-attempt.schema.json`, `ai-tutor-feedback.schema.json` and `learner-progress.schema.json`.
- Added `23-product-schemas/README.md` (entity map, academy mapping, AI tutor contract) and `23-product-schemas/examples.md` with six worked instances that validate against their schemas.

### Changed

- The schemas formalise the objects previously sketched in prose in APP_INTEGRATION_PLAN.md and the fields in the progress tracker, encoding the marking-guide bands, spoken-rubric dimensions and automatic caps as schema.
- Updated MASTER_INDEX.md with a Product Integration section and README.md repository map with `23-product-schemas/`.
- Updated ROADMAP.md to mark the product-layer schemas complete.
- Bumped VERSION to 0.8.0.

## 2026-07-01 (scenario bank split)

### Added

- Added `20-scenario-bank/scenarios/` with five themed scenario sets (ten scenarios each) split out of the operational scenario bank for phone-first study: fire-and-water, asbestos-electrical-lifting, height-contractors-coshh, waste-estate-power and assets-evidence-board.

### Changed

- Converted `20-scenario-bank/fm-operational-scenario-bank.md` into a phone-first themed index that links to the five sets, preserving all inbound links and the scenario response structure; content is unchanged (50 scenarios verified).
- Updated ROADMAP.md and FIX_LIST.md to record the scenario bank split, leaving only the boardroom simulation to split.
- Bumped VERSION to 0.7.0.

## 2026-07-01 (mobile-first bank split)

### Added

- Added `19-interview-prep/question-bank/` with ten themed question sets (ten questions each) split out of the interview bank for phone-first study: health-safety-risk, fire-safety, water-hygiene, asbestos-building-fabric, electrical-critical-systems, work-equipment-lifting-height, contractor-management, asset-management-budget, visitor-attraction-longleat and leadership-board-communication.

### Changed

- Converted `19-interview-prep/longleat-interview-question-bank.md` into a phone-first themed index that links to the ten sets, preserving all inbound links; content is unchanged and now easier to study one theme per session.
- Refreshed `RELEASE_NOTES.md` to version 0.6.0 with a cumulative summary and current known limitations (previously frozen at 0.1.0).
- Updated ROADMAP.md and FIX_LIST.md to record the interview bank split and the remaining scenario-bank and boardroom-simulation splits.
- Bumped VERSION to 0.6.0.

## 2026-06-30 (interview completion and study aids)

### Added

- Added `19-interview-prep/longleat-boardroom-roleplay-prompts.md`: six live pressure scenarios with in-character interviewer lines, press-harder follow-ups, "what good sounds like" notes and a reader scoring card.
- Added `17-marking-guides/spoken-answer-rubric.md`: a six-dimension /24 rubric for spoken answers with bands, automatic caps, delivery tells and AI-tutor notes.
- Added `21-flashcards/flashcard-bank.md`: phone-first recall cards for all twelve modules plus cross-cutting principles, tagged to modules.
- Added `22-study-plans/30-day-study-plan.md`: a paced four-week route through the modules, workbook, mock exams and final assessment.
- Added `22-study-plans/progress-tracker.md`: a self-assessment tracker with module, assessment and interview tables, a weak-tag watchlist, a readiness checklist and the suggested FM Control Hub progress fields.

### Changed

- Updated MASTER_INDEX.md with a Study Aids section and the new role-play and spoken-rubric links.
- Updated README.md repository map with `21-flashcards/` and `22-study-plans/`.
- Updated ROADMAP.md to mark the interview layer complete and add the mobile learning layer.
- Updated TODO.md to mark the flashcard bank, progress tracker, 30-day plan, role-play prompts and spoken rubric complete.
- Updated FIX_LIST.md with the 0.5.0 fixes.
- Bumped VERSION to 0.5.0.

## 2026-06-30 (interview layer)

### Added

- Added `19-interview-prep/7-day-longleat-crash-plan.md`: an intensive, standalone seven-day interview plan with three daily blocks (morning learn, commute drill, evening spoken practice) that uses the modules, workbook, mock exams, final assessment, interview/scenario banks and boardroom simulation, plus a night-before checklist.
- Added `19-interview-prep/longleat-star-answer-bank.md`: worked STAR answers across eight Longleat themes, five core stories to prepare, a spoken-answer self-check and two opening answers.

### Changed

- Updated MASTER_INDEX.md to list the crash plan and STAR answer bank under practice banks.
- Updated ROADMAP.md to mark the crash plan and STAR bank complete in the interview layer.
- Updated TODO.md to mark the 7-day crash plan and STAR answer bank complete.
- Bumped VERSION to 0.4.0.

## 2026-06-30 (assessment layer)

### Added

- Added the workbook layer: `14-workbook/` with an index and a workbook file for each of Modules 1 to 12, every file holding knowledge/application/judgement questions, model answer points and per-module marking criteria.
- Added `17-marking-guides/marking-guide.md`: a single course marking standard with scoring bands, four marking strands, automatic caps, red/green flags and AI-tutor rubric notes.
- Added `16-mock-exams/`: an index plus Mock Exam 1 and Mock Exam 2, each a timed 90-minute, three-section paper with model answer pointers.
- Added `18-final-assessment/final-assessment.md`: a 180-minute capstone across compliance, money/assets, leadership/strategy and an integrated peak-season scenario, with a result-record table.

### Changed

- Updated MASTER_INDEX.md with an Assessment section linking the workbook, mock exams, marking guide and final assessment.
- Updated ROADMAP.md to mark the assessment layer complete and refocus next priorities on mobile polish and the product layer.
- Updated TODO.md to mark all Phase 2 workbook and assessment items complete.
- Bumped VERSION to 0.3.0.

## 2026-06-30

### Added

- Added Module 9: Budgeting and Finance (opex/capex, defensible budgets, whole-life cost, variance and no-surprises forecasting).
- Added Module 10: Leadership and Communication (leading mixed teams, communicating up and down, hard conversations, incident communication).
- Added Module 11: Strategic FM (operational/tactical/strategic levels, business alignment, KPIs and data, lifecycle planning, in-house versus outsource).
- Added Module 12: Estate Management (grounds, boundaries, drainage, heritage, multiple buildings and estate-wide risk).
- Completed the full twelve-module core course (Modules 1 to 12 plus the Longleat simulation).

### Changed

- Updated MASTER_INDEX.md to list Modules 9 to 12.
- Updated ROADMAP.md to show the core course as complete and refocus next content on the assessment layer.
- Updated TODO.md to mark Modules 9 to 12 complete.
- Bumped VERSION to 0.2.0.

## 2026-06-24

### Added

- Created production course roadmap.
- Added README with mission, learning outcomes, module structure and product integration vision.
- Added TODO tracker with completion rule.
- Added Wave 1 course orientation.
- Added Wave 1 Module 1: Facilities Management Principles.
- Added Wave 1 Module 2: Risk Management.
- Added Wave 2 Module 3: Health & Safety Management.
- Added Wave 2 Module 4: Fire Safety.
- Added Wave 2 Module 5: Water Hygiene.
- Added Wave 3 Module 6: Building Systems.
- Added Wave 3 Module 7: Asset Management.
- Added Wave 3 Module 8: Contractor Management.
- Added Wave 3 Module 13: Longleat Boardroom Simulation.
- Added Wave 4 Longleat interview question bank with 100 production questions.
- Added Wave 4 FM operational scenario bank with 50 production scenarios.
- Added Wave 5 navigation and product readiness layer.
- Added master index, quick start, roadmap, glossary and tag taxonomy.
- Added FM Control Hub usage and Longleat interview prep usage pages.
- Added AI/RAG metadata block to the repository README.
- Added Wave 6 quality audit, fix list, release notes and VERSION 0.1.0.
- Added Wave 7 app integration plan for learner journeys, assessments, AI tutor and Longleat interview prep.
- Set next target version to 0.2.0 in the roadmap.
- Added missing AI/RAG metadata blocks to early course modules.
- Corrected README repository map for interview and scenario bank folders.
- Updated TODO tracker to mark completed Wave 1 course items.
- Updated TODO tracker to mark completed Wave 2 course modules.
- Updated TODO tracker to mark completed Wave 3 course modules and simulation.
- Updated TODO tracker to mark completed Wave 4 interview and scenario banks.
- Updated TODO tracker to mark completed Wave 5 navigation and readiness items.
- Updated TODO tracker to mark completed Wave 6 quality audit and release readiness items.
- Updated TODO tracker to mark completed Wave 7 app integration planning items.

### Production Notes

- This is not an official IWFM qualification.
- This repo is a practical Level 4-style learning framework.
- No placeholder modules are permitted.
- Every future completed task must update this changelog and `TODO.md`.
- Every completed task must be committed and pushed.
