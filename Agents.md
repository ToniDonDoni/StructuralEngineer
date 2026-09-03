# Agent Instructions

This repository follows the engineering-task and Spec-Driven TDD workflows
defined in:

- `Skills/ENGINEERING-TASK-SOLVING-GUIDE.md`
- `Skills/spec-driven-tdd/SKILL.md`

Before changing this repository, the implementer must inspect all guidance
files in `Skills/` relevant to the task and follow their workflows. The
canonical task specification is:

- `Tasks/001-garage-ventilation/spec.md`

Required workflow:

1. Present the canonical specification and obtain explicit user approval.
2. Write proving RED tests and demonstrate target-specific failure.
3. Obtain an independent `RED_REVIEW: PASS`.
4. Implement the minimum GREEN solution.
5. Run proving and relevant regression tests.
6. Obtain an independent `GREEN_REVIEW: PASS`.

Do not begin RED or GREEN work before the required approval and review gates.
Do not implement directly on `main`; use a dedicated feature branch. Commit
messages must contain ASCII characters only.
