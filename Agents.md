# Agent Instructions

This repository follows the unified structural-engineering Spec-Driven TDD workflow defined in:

- `Skills/structural-engineering-spec-driven-tdd/SKILL.md`

Before changing this repository, the implementer must read and follow that skill.

Repository layout:

- `Skills/` contains agent workflow skills.
- `Tasks/<NNN-short-task-name>/` contains task input and specification files, including raw user input in `TASK.md` and the approved `spec.md`.
- `Solutions/<NNN-short-task-name>/` contains the solution for the corresponding task, including RED and GREEN stage artifacts and results.

Required workflow:

1. Build and present the engineering specification, including the applicable normative basis, and obtain explicit user approval.
2. Write proving RED tests covering every approved acceptance criterion and demonstrate target-specific failure.
3. Obtain an independent `RED_REVIEW: PASS`.
4. Implement the minimum GREEN solution.
5. Run proving and relevant regression tests.
6. Obtain an independent `GREEN_REVIEW: PASS`.

Do not implement directly on `main`; use a dedicated feature branch. Commit messages must contain ASCII characters only.
