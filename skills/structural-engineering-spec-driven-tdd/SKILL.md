---
name: structural-engineering-spec-driven-tdd
description: "Spec-Driven Test-Driven Development framework for structural and construction engineering tasks under Russian construction regulations: independently reviewed spec, human approval, independently reviewed RED and GREEN."
license: MIT
metadata:
  version: 1.2.5
  author: GPT-5.6 Sol
---

## How to use

Copy `SKILL.md` to `<agent_skill_directory>/structural-engineering-spec-driven-tdd/`.

The workflow may start in either of two ways.

### 1. User provides the task directly

The user gives the engineering task in chat, for example:

`Use structural-engineering-spec-driven-tdd skill. Solve this task: <task>`

If no task directory exists yet, the Implementer:

1. determines the next task number;
2. creates `tasks/<NNN-short-task-name>/` using a concise task name derived from the user request;
3. writes the user's raw task input to `tasks/<NNN-short-task-name>/TASK.md`;
4. uses that `TASK.md` as the source input for Spec formation.

### 2. `TASK.md` already exists

The user may create the task directory and `TASK.md` manually before invoking the skill.

In that case, the Implementer uses the existing task directory and existing `TASK.md`.

Example:

`Use structural-engineering-spec-driven-tdd skill. Work from tasks/002-foundation-strengthening/TASK.md according to the skill.`

`TASK.md` contains the raw, unapproved user input. The Implementer reads it, forms the approval-ready engineering spec, sends that draft to an independent Reviewer for `SPEC_REVIEW`, and shows the reviewed spec to the user only after `SPEC_REVIEW: PASS`.

After explicit user approval, the Implementer persists the approved version in the same task directory as `SPEC.md`.

Only then does RED begin.

The task flow is:

`User Input -> TASK.md -> Approval-ready Spec -> SPEC_REVIEW -> User Approval -> SPEC.md -> RED -> RED_REVIEW -> GREEN -> GREEN_REVIEW`

# Structural Engineering Spec-Driven TDD

Use this workflow for structural, construction, and building-engineering tasks.

For engineering tasks, the spec establishes what must be true. SPEC_REVIEW independently checks the task interpretation and normative basis before the user is asked to approve it. RED defines how each approved acceptance criterion is proved. GREEN performs the engineering calculation or implementation.

## Workflow

1. **User** provides an engineering task directly or through an existing task-local `TASK.md`.
2. **Implementer** ensures the task has a task-local `TASK.md`: create the next numbered task directory and `TASK.md` from direct user input when needed, or reuse the existing task directory when already present.
3. **Implementer** reads `TASK.md`, analyzes the task, identifies engineering objects, processes, and conditions, finds the applicable Russian normative basis, identifies required inputs and assumptions, and produces a compact approval-ready spec with a complete acceptance-criteria list.
4. **Reviewer**, running independently from the Implementer, performs `SPEC_REVIEW` of the task interpretation and normative basis.
5. On `SPEC_REVIEW: FAIL`, the Implementer fixes the approval-ready spec and requests independent `SPEC_REVIEW` again until `SPEC_REVIEW: PASS`.
6. **Implementer** presents the reviewed approval-ready spec to the User.
7. **User** explicitly approves the spec.
8. **Implementer** persists the approved spec as task-local `SPEC.md` and commits it.
9. **Implementer** writes RED tests covering every approved acceptance criterion and proves they fail for the intended reason.
10. **Reviewer**, running independently from the Implementer, performs `RED_REVIEW`.
11. On `RED_REVIEW: FAIL`, the Implementer fixes RED, reruns it, commits, and requests independent review again until `RED_REVIEW: PASS`.
12. **Implementer** performs the minimum GREEN calculation or implementation required by the approved spec.
13. **Reviewer**, again independently, performs `GREEN_REVIEW`.
14. On `GREEN_REVIEW: FAIL`, the Implementer fixes GREEN, reruns relevant tests, commits, and requests independent review again until `GREEN_REVIEW: PASS`.
15. The task is complete only after `GREEN_REVIEW: PASS` and the original engineering task is demonstrably resolved.

Work on a dedicated feature branch unless the user explicitly requests otherwise. Never implement directly on the repository's main/default branch.

## Roles

### Implementer

The Implementer owns task analysis, spec formation, SPEC_REVIEW fixes, user approval, RED, RED fixes, GREEN, GREEN fixes, and completion.

### Reviewer

The Reviewer is a genuinely independent delegated agent/session. The Implementer must not merely switch hats.

The Reviewer must not edit the spec, RED tests, or GREEN solution and must not fix findings or commit changes. It may inspect repository content, normative references, calculations, tests, CI results, and other evidence required for review.

The Reviewer performs only:

- `SPEC_REVIEW`
- `RED_REVIEW`
- `GREEN_REVIEW`

## Spec

The purpose of the Spec stage is to produce a compact engineering contract that an independent Reviewer can check and the user can inspect and approve before any RED test or GREEN calculation is written.

The source user input is the task-local `TASK.md`. `TASK.md` is unapproved input and is not the canonical spec.

The approved spec defines **what must be true**. It does not define the proving tests or implementation.

For structural and construction-engineering tasks in the Russian Federation, the spec must be based on the applicable Russian construction regulations identified during task analysis.

The normative basis may include:

- **SP — Sets of Rules (`Своды правил`)**
- **SNiP — Construction Norms and Rules (`Строительные нормы и правила`)**
- **GOST — National or Interstate Standards**
- applicable technical regulations;
- applicable fire-safety or sanitary regulations;
- other materially relevant Russian normative documents.

Use authoritative official sources when available, including the Ministry of Construction of the Russian Federation document catalogue:

`https://minstroyrf.gov.ru/docs/`

### Spec formation

The Implementer performs enough engineering and regulatory research to produce the following approval artifact.

#### 1. Task summary

State what engineering problem must be solved and preserve the user's explicit requirements and constraints.

#### 2. Engineering objects and processes

Identify the objects, processes, and conditions that materially affect the task.

Examples include structural members, systems, loads, materials, supports, construction or strengthening processes, operating conditions, environmental conditions, fire compartments, interfaces, or other objects/processes that change a normative requirement, calculation branch, or engineering conclusion.

Build:

`User Task -> Engineering Objects / Processes`

#### 3. Normative Basis

For every material engineering object or process, identify the applicable Russian normative documents and relevant clauses.

For each material requirement record:

- document identifier and title;
- applicable edition/revision and amendments when relevant;
- exact section or clause when practical;
- official source;
- verification date;
- requirement imposed by that clause.

Build:

`Engineering Object / Process -> Regulation -> Clause -> Requirement`

The **Normative Basis is mandatory in the approved spec**. Every SP, SNiP, GOST, or other normative document materially required to solve the task must be listed.

#### 4. Inputs

List the known material inputs and their origins.

Use these origin categories:

- `user_provided`
- `project_provided`
- `regulatory`
- `design_assumption`
- `illustrative_verification_input`

A required factual value that is not available remains `missing`.

A value supplied by the user remains user-provided even when a regulation later uses it in a calculation.

#### 5. Missing inputs and assumptions

From the applicable regulations and calculation requirements, identify any additional input that is required but absent from the original task.

For every such input, either:

- keep it `missing`; or
- propose an explicit `design_assumption` for a conditional calculation or applicability scenario.

A design assumption must state its value/condition, engineering basis, and which result or branch depends on it. Results depending on assumptions are conditional.

When a regulatory threshold controls a branch, use a meaningful boundary/minimum value for the intended scenario unless another value has an engineering justification.

#### 6. Acceptance criteria

Derive a complete acceptance-criteria list from:

1. the user's requirements; and
2. every material regulatory requirement in the Normative Basis.

Assign stable IDs:

`AC1`, `AC2`, `AC3`, ...

Acceptance criteria describe objectively verifiable engineering outcomes or properties.

Examples:

- all required loads are included;
- the governing load combination is selected correctly;
- design resistance is not less than design action;
- a regulatory limit is not exceeded;
- a required stability check is performed when applicable;
- an applicability branch is derived from accepted inputs;
- a missing factual input is not presented as project data;
- an assumption-dependent conclusion remains conditional;
- a material calculation is dimensionally consistent and reproducible;
- every material normative requirement is represented in the accepted result.

The spec traceability stops at:

`Engineering Object / Process -> User/Regulatory Requirement -> Acceptance Criterion`

Defining proving tests belongs to RED.

### SPEC_REVIEW — Reviewer agent

Before the approval-ready spec is shown to the user, an independent Reviewer performs `SPEC_REVIEW`.

The independent Reviewer reads, in this order:

1. `SKILL.md`;
2. the original user task from `TASK.md`;
3. the approval-ready spec draft, including its Engineering Objects / Processes and Normative Basis.

`SPEC_REVIEW` is deliberately narrow. The Reviewer checks only:

- whether the engineering objects, processes, and material conditions extracted from the task are accurate, relevant, and sufficiently complete for the task;
- whether any material object/process was invented, omitted, or materially misclassified;
- whether every normative document selected for the task is actually relevant and applicable to the claimed object, process, or requirement;
- whether document identifiers, titles, scopes, editions/revisions, amendments, and current status are accurate and up to date;
- whether cited sections/clauses are relevant to the requirement attributed to them;
- whether authoritative sources support the identity, status, and applicability claims made for the normative documents.

`SPEC_REVIEW` does **not** approve the engineering solution, choose a design method for the user, define RED tests, or perform GREEN calculations. User approval remains a separate mandatory stage after `SPEC_REVIEW: PASS`.

`SPEC_REVIEW: PASS` is forbidden when a material task object/process is missing or materially wrong, or when a material normative document is obsolete without justification, incorrectly identified, irrelevant, inapplicable, or used for a requirement outside its actual scope.

Reviewer returns:

- `SPEC_REVIEW: PASS`
- `SPEC_REVIEW: FAIL`
- `SPEC_REVIEW: NEEDS_CLARIFICATION`
- `SPEC_REVIEW: BLOCKED`

On `FAIL`, the Implementer corrects the approval-ready spec and requests independent `SPEC_REVIEW` again.

The approval-ready spec may be shown to the user for approval only after `SPEC_REVIEW: PASS`.

### Spec target shown to the user

The reviewed approval-ready spec must contain exactly the information needed to agree on the engineering task before testing or implementation:

- **Task Summary**
- **Engineering Objects and Processes**
- **Normative Basis** — participating SP/SNiP/GOST/other regulations and relevant clauses
- **Known Inputs** and their origins
- **Missing Inputs**
- **Design Assumptions**, if proposed
- **Acceptance Criteria (`AC1...ACN`)**
- **RED proof boundary** — which public engineering artifact/result will later be tested and why it is currently absent or incomplete
- **GREEN condition** — what accepted engineering result will constitute completion

After `SPEC_REVIEW: PASS`, the approval-ready spec is shown to the user before it becomes canonical.

After explicit user approval, persist the canonical approved spec in the same task directory as `SPEC.md`.

Commit `SPEC.md` with an ASCII-only commit message before RED.

## Mid-work requirement changes

If the user adds or changes a requirement after work has started, preserve the approved requirement history.

Append the new raw user requirement to task-local `TASK.md` as:

`ADDITION: <requirement>`

Identify affected objects/processes/norms/inputs/ACs and update the approval-ready spec. If the change affects engineering objects, processes, conditions, or the Normative Basis, obtain a new independent `SPEC_REVIEW: PASS` for the affected spec before presenting it to the user for renewed approval. Replan only the affected RED/GREEN work. Obtain renewed user approval unless further approval was explicitly waived. After approval, update the canonical `SPEC.md` before continuing affected RED/GREEN work.

## RED

After user approval and persistence of `SPEC.md`, the Implementer defines the proving tests.

**Every acceptance criterion in the approved spec must have identifiable RED proving coverage.**

Build the complete mapping:

`Acceptance Criterion -> Proving Test -> Decisive Assertion / Expected Result`

No approved acceptance criterion may be omitted.

For engineering tasks, RED tests should independently prove the engineering properties required by the approved ACs, including where applicable:

- normative applicability;
- input provenance;
- required loads/actions;
- units and dimensional consistency;
- governing-case selection;
- formula or method relation required by the approved spec;
- rounding where it can change compliance;
- relevant threshold/boundary behavior;
- reproducibility of material numerical results;
- conditional treatment of design assumptions.

A test should verify the engineering relation rather than merely a self-declared flag when the relation can be checked directly.

Every proving test must clearly state the behavior under test and expected result.

RED must fail specifically because the approved engineering behavior or result is missing or incorrect. Syntax errors, missing dependencies, broken fixtures, environment failures, or unrelated defects are invalid RED.

Run the narrow proving command and commit RED with an ASCII-only commit message.

### RED_REVIEW — Reviewer agent

The independent Reviewer reads, in this order:

1. `SKILL.md`;
2. the original user task from `TASK.md`;
3. the approved `SPEC.md` and complete `AC1...ACN` list;
4. the RED commits/tests;
5. proving evidence.

The Reviewer checks that:

- RED covers **every approved acceptance criterion**;
- each cited test semantically proves the criterion rather than merely mentioning it;
- the test boundary is practical and sufficiently high-level;
- target-specific RED failure is demonstrated;
- RED contains no GREEN implementation;
- test setup and evidence are trustworthy;
- applicable engineering/normative properties required by each AC are actually tested.

Before issuing the verdict, the Reviewer must provide exactly one row for every approved acceptance criterion:

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | `test_...` proves ... | PASS / FAIL |
| AC2 | `test_...` proves ... | PASS / FAIL |
| ... | ... | ... |

The number of rows must equal the number of approved acceptance criteria.

`RED_REVIEW: PASS` is forbidden if any AC is missing, lacks proving coverage, or is not actually proved by the cited test.

Reviewer returns:

- `RED_REVIEW: PASS`
- `RED_REVIEW: FAIL`
- `RED_REVIEW: NEEDS_CLARIFICATION`
- `RED_REVIEW: BLOCKED`

On `FAIL`, the Implementer fixes RED, reruns it, commits, and requests review again.

GREEN begins only after `RED_REVIEW: PASS`.

## GREEN

After RED review passes, the Implementer performs the minimum engineering calculation or implementation required by the approved spec and reviewed RED.

GREEN may contain the actual:

- calculations;
- formulas/methods;
- numerical substitutions;
- intermediate results;
- applicability decisions;
- engineering checks;
- selected parameters;
- final engineering report/result.

Use the inputs and assumptions approved by the spec. Missing factual values remain missing unless an approved design assumption is used. Results depending on assumptions remain conditional.

For material numerical calculations, preserve enough evidence to reproduce the result from recorded inputs and the approved method.

Run proving tests and relevant regression tests, then commit with an ASCII-only commit message.

### GREEN_REVIEW — Reviewer agent

The independent Reviewer reads, in this order:

1. `SKILL.md`;
2. `TASK.md`;
3. the approved `SPEC.md` and complete AC list;
4. reviewed RED;
5. GREEN commits and engineering result.

The Reviewer checks that:

- every approved AC has direct engineering/test evidence;
- reviewed RED now passes for the intended reason;
- applicable normative requirements are satisfied;
- inputs and assumptions match the approved spec;
- units, dimensions, calculations, rounding, boundary cases, and result reproducibility are correct where material;
- the reported governing case is actually governing where applicable;
- assumptions remain conditional;
- the accepted result actually resolves the original engineering task.

Before issuing the verdict, the Reviewer must provide exactly one row for every approved acceptance criterion:

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | engineering/test evidence ... | PASS / FAIL |
| AC2 | engineering/test evidence ... | PASS / FAIL |
| ... | ... | ... |

`GREEN_REVIEW: PASS` is forbidden if any approved AC is missing or lacks sufficient evidence.

Reviewer returns:

- `GREEN_REVIEW: PASS`
- `GREEN_REVIEW: FAIL`
- `GREEN_REVIEW: NEEDS_CLARIFICATION`
- `GREEN_REVIEW: BLOCKED`

The workflow is complete only after `GREEN_REVIEW: PASS` and explicit confirmation that the original engineering task is resolved by the accepted outcome.

## Constraints

Use the project's existing architecture and conventions.

Commit messages are ASCII-only.

Passing tests never replace independent SPEC/RED/GREEN review.

## Completion

Report the approved spec source, SPEC_REVIEW verdict, RED result/commit, GREEN result/commit, final review verdict, principal normative basis, important assumptions or unresolved inputs, and how the accepted result resolves the original engineering task.

# Addendum — Review report examples

## SPEC_REVIEW example

```text
SPEC_REVIEW

Task interpretation: PASS
Normative basis: FAIL

SP 16.13330 is a steel-structures standard and does not support the claimed reinforced-concrete strengthening requirement.

SPEC_REVIEW: FAIL
```

## RED_REVIEW example

```text
RED_REVIEW

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | `test_required_loads` proves all required loads are included | PASS |
| AC2 | `test_governing_combination` proves governing-case selection | PASS |
| AC3 | No proving test covers the required stability check | FAIL |

AC3 is not covered by RED.

RED_REVIEW: FAIL
```

## GREEN_REVIEW example

```text
GREEN_REVIEW

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | Required loads are present and the reviewed RED test passes | PASS |
| AC2 | The reported governing combination matches the calculated governing effect | PASS |
| AC3 | Stability calculation satisfies the applicable requirement | PASS |

GREEN_REVIEW: PASS
```

## Coverage rule

A review verdict never replaces the acceptance-list summary.

The Reviewer establishes:

`Acceptance Criterion -> Test / Engineering Evidence -> Verdict`
