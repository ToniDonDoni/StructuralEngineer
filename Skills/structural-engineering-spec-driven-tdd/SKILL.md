---
name: structural-engineering-spec-driven-tdd
description: "Spec-Driven Test-Driven Development framework for structural and construction engineering tasks under Russian construction regulations: human-approved spec, independently reviewed RED and GREEN."
license: MIT
metadata:
  version: 1.1.0
  author: GPT-5.6 Sol
---

## How to use

Copy `SKILL.md` to `<agent_skill_directory>/structural-engineering-spec-driven-tdd/`.

Ask the agent:

`Use structural-engineering-spec-driven-tdd skill and solve this engineering task.`

Then the agent says:

`This is the spec... Approve?`

Then say:

`ok`

Or say:

`ok, and do not request any further user approval until the work is complete.`

# Structural Engineering Spec-Driven TDD

Use this workflow for structural, construction, and building-engineering tasks.

The workflow preserves the standard Spec-Driven TDD sequence:

`User Task -> Spec -> User Approval -> RED -> RED_REVIEW -> GREEN -> GREEN_REVIEW`

For engineering tasks, specification formation additionally establishes:

`Task -> Engineering Objects -> Normative Basis -> Inputs -> Missing Inputs / Assumptions -> Acceptance Criteria -> Compliance Tests`

## Workflow

1. **User** requests an engineering calculation, design, verification, or other construction-related task.
2. **Implementer** inspects the existing repository and task, performs the minimum engineering and regulatory research required to formalize the task, and writes a concise spec with acceptance criteria, RED proof, and GREEN condition.
3. **User** explicitly approves that spec.
4. **Implementer** writes RED tests and proves they fail for the intended reason.
5. **Reviewer**, running as a separate delegated agent/session, performs `RED_REVIEW` against the approved spec.
6. **Implementer** writes the minimum GREEN engineering solution and runs proving plus relevant regression tests.
7. **Reviewer**, again independently delegated, performs `GREEN_REVIEW` and verifies the final outcome solves the original engineering task.
8. The task is complete only after `GREEN_REVIEW: PASS` and the original user task is demonstrably resolved.

Work sequentially on a dedicated feature branch for the change unless the user explicitly asks otherwise. Never implement directly on the repository's main/default branch.

## Roles

There are exactly two agent roles.

### Implementer

The Implementer is the single primary agent and owns the whole forward path: repository inspection, spec formalization, engineering and regulatory research required for the spec, user approval, RED, fixes from RED review, GREEN implementation, fixes from GREEN review, and completion.

### Reviewer

The Reviewer is a genuinely independent delegated agent/session.

Launch it through the available delegation mechanism as a separate worker/session from the Implementer; the Implementer must not merely switch hats.

If an independent Reviewer cannot be launched because of platform or infrastructure limitations, stop the workflow and report the blocker rather than silently replacing independent review with Implementer self-review.

The Reviewer must not edit production code, tests, the engineering solution, or the spec and must not fix findings or commit changes.

It may read repository content, engineering artifacts, normative references, calculations, test evidence, CI results, or other material needed to validate the review.

The Reviewer performs only:

- `RED_REVIEW`
- `GREEN_REVIEW`

## Spec

If the project already has a `specs/` directory, keep one flat numbered spec per change there: `specs/spec_<number>.md`, for example `specs/spec_001.md`. Do not create per-spec subdirectories.

If the project has no `specs/` directory, do not introduce one only for this workflow. Instead, preserve the complete user-approved spec in the primary proving test description so the test remains self-contained and reviewable.

The final spec shown to the user for approval must be compact enough to read quickly, but it must preserve the full substance of the user's engineering problem and requirements.

For structural and construction-engineering tasks in the Russian Federation, the specification must be based on the applicable Russian construction regulations identified during spec formation.

The normative basis may include:

- **SP — Sets of Rules (`Своды правил`)**
- **SNiP — Construction Norms and Rules (`Строительные нормы и правила`)**
- **GOST — National or Interstate Standards**
- applicable technical regulations;
- applicable fire-safety regulations;
- applicable sanitary regulations;
- other mandatory or materially relevant Russian engineering regulations.

Use authoritative official regulatory sources when available, including the Ministry of Construction of the Russian Federation document catalogue:

`https://minstroyrf.gov.ru/docs/`

The approval version of the spec must include:

- a concise but complete statement of the original engineering task expressed by the user;
- all explicit requirements, constraints, and required observable engineering behavior from the user's request;
- the engineering objects and conditions relevant to the task;
- a mandatory **Normative Basis** listing every SP, SNiP, GOST, technical regulation, or other regulatory document materially required to solve the task;
- for every material normative requirement: document identifier, title, applicable edition/revision, applicable amendments when relevant, exact section or clause, official source, verification date, and the engineering object or requirement covered;
- known user/project inputs and their origins;
- additional inputs required by applicable regulations or calculations but absent from the original user request;
- explicit preliminary engineering assumptions where necessary;
- proposed acceptance criteria, each with a stable identifier such as `AC1`, `AC2`, `AC3`;
- important applicability branches or edge cases when useful;
- RED proof: what test boundary should prove the engineering behavior and why it should fail before implementation;
- GREEN condition: what must pass after implementation.

### Engineering task specification formation

For a structural or construction-engineering task, form the specification in the following order.

### 1. Extract engineering objects

Identify all engineering objects explicitly or implicitly involved in the user's task.

Examples include:

- buildings;
- rooms and zones;
- structural elements;
- beams;
- columns;
- slabs;
- walls;
- foundations;
- connections;
- supports and restraints;
- loads and actions;
- materials;
- ventilation systems;
- ducts;
- fans;
- gates;
- fire compartments;
- engineering equipment;
- environmental conditions;
- operating conditions;
- construction stages;
- interfaces between systems or elements.

Also identify conditions that can materially affect:

- applicable regulations;
- applicable clauses;
- calculation method;
- calculation branch;
- load combination;
- boundary condition;
- required engineering check;
- final engineering conclusion.

Build:

`User Task -> Engineering Objects`

If something materially changes a regulatory requirement, applicability branch, calculation, or conclusion, include it in the task model even if the user did not explicitly describe it as an object.

### 2. Preserve user and project inputs

Extract all values and conditions already supplied by the user or available from factual project documentation.

Every material input must have an explicit origin or be marked missing.

Use the following canonical origin vocabulary:

- `user_provided`
- `project_provided`
- `regulatory`
- `design_assumption`
- `illustrative_verification_input`
- `calculated_output`

Use the following canonical states where applicable:

- `available`
- `missing`
- `conditional`
- `verification_only`
- `calculated`

Canonical meanings:

| Origin | Meaning | Normal state |
|---|---|---|
| `user_provided` | Explicitly supplied by the user or original task | `available` |
| `project_provided` | Factual value from drawings, reports, BIM, survey, equipment data, or another project source | `available` |
| `regulatory` | Value or rule obtained from an applicable normative source | `available` |
| `design_assumption` | Explicit preliminary assumption used because factual project data is unavailable | `conditional` |
| `illustrative_verification_input` | Synthetic value used only to verify a calculation or compliance-test relation | `verification_only` |
| `calculated_output` | Result derived from accepted inputs | `calculated` |

A required value for which no factual input or approved assumption exists has state:

`missing`

A value supplied by the user remains `user_provided` even when an SP, SNiP, or GOST later uses that value in a calculation.

Example:

If the user supplied:

`design CO concentration = 20 mg/m3`

the value remains `user_provided`.

The rule defining how it participates in the calculation may independently have `regulatory` origin.

### 3. Provenance transitions

When information becomes available, preserve explicit provenance transitions.

A missing input may become:

`missing -> user_provided / available`

or:

`missing -> project_provided / available`

when factual information is supplied.

For preliminary engineering work it may become:

`missing -> design_assumption / conditional`

When factual data later replaces an assumption:

`design_assumption / conditional -> user_provided or project_provided / available`

Every dependent applicability decision and engineering calculation must then be recomputed.

`illustrative_verification_input` remains verification-only.

`calculated_output` remains distinguishable from independent factual input.

### 4. Determine the Russian Normative Basis

For every engineering object, identify all Russian construction regulations required to design, calculate, or verify that object.

Search the applicable:

- SP;
- SNiP or applicable updated SP edition;
- GOST;
- technical regulations;
- fire-safety regulations;
- sanitary regulations;
- other applicable normative documents.

For every material normative requirement record:

- document identifier;
- document title;
- applicable edition or revision;
- applicable amendments where relevant;
- exact section or clause when practical;
- official source;
- verification date;
- engineering object covered;
- requirement imposed by that clause.

Build:

`Engineering Object -> SP/SNiP/GOST -> Clause -> Regulatory Requirement`

The **Normative Basis is a mandatory part of the approved spec**.

Every SP, SNiP, GOST, or other normative document that materially participates in solving the engineering task must be explicitly listed.

### 5. Map regulatory requirements to engineering objects

For every identified engineering object, determine which requirements from the Normative Basis apply to it.

An object may map to multiple regulatory clauses.

A regulatory clause may affect multiple engineering objects.

Build:

`Engineering Object -> Regulation Clause -> Regulatory Requirement`

Examples:

`Beam -> applicable SP -> bending resistance clause -> bending resistance requirement`

`Beam -> applicable SP -> stability clause -> stability requirement`

`Garage ventilation -> SP 113.13330.2023 -> clause 8.3.10 -> harmful-emission assimilation requirement`

Do not collapse a multi-clause engineering object into one arbitrary regulatory row.

### 6. Determine regulatory applicability

For every conditional regulatory requirement, identify the conditions under which it applies.

Examples:

- structural material;
- support condition;
- span;
- slenderness;
- heated or unheated condition;
- underground or above-ground condition;
- number of parking spaces;
- fire-compartment configuration;
- duct crossing;
- seismic region;
- environmental conditions;
- operating regime.

For every material applicability branch identify:

- regulation clause;
- applicability condition;
- inputs required to evaluate it;
- possible branch outcomes.

Build:

`Project Inputs -> Applicability Condition -> Regulatory Branch`

Example:

`garage_location_type + parking_space_count -> underground AND >25 -> 100% reserve required`

### 7. Identify additional required inputs

Compare the original task inputs with the inputs required by:

- identified regulations;
- applicability branches;
- calculation procedures;
- acceptance criteria.

Identify every additional value or object required to solve the task correctly.

Examples include:

- dimensions;
- support conditions;
- material properties;
- parking-space count;
- outdoor temperature;
- indoor temperature;
- fire-compartment data;
- soil parameters;
- emission rates;
- maximum hourly entry count;
- load category;
- restraint spacing;
- section properties.

The spec must explicitly distinguish:

`known factual inputs`

from:

`required but currently unknown inputs`

### 8. Define missing-input handling and engineering assumptions

For every required but unavailable input, determine whether:

1. the affected calculation or applicability result remains unresolved until factual information becomes available; or
2. an explicit preliminary `design_assumption` may be introduced to perform a conditional calculation or evaluate a regulatory branch.

A design assumption must record:

- assumed object or parameter;
- assumed value or condition;
- origin `design_assumption`;
- state `conditional`;
- engineering basis;
- calculation or applicability branch enabled by it;
- downstream results that depend on it.

For example:

If a regulatory branch is:

`parking_space_count > 25`

and a preliminary scenario specifically evaluates the first applicable case:

`parking_space_count = 26`

may be used as:

`design_assumption / conditional`

When a regulatory threshold determines a branch, prefer a meaningful boundary or minimum value needed to exercise the intended scenario unless another value has an engineering justification.

### 9. Keep requirement origin separate from input origin

Preserve requirement origin independently from calculation-input origin.

Example:

SP clause 8.3.10 may impose a regulatory calculation requirement.

That requirement remains:

`regulatory`

even if an illustrative calculation uses:

`design_assumption`

or:

`illustrative_verification_input`

for some numerical inputs.

A user-origin requirement remains user-origin unless a normative source independently establishes the same requirement.

### 10. Convert the Normative Basis into engineering requirements

For every applicable normative clause, derive the engineering requirement the future solution must satisfy.

Build:

`Engineering Object -> Regulation Clause -> Regulatory Requirement -> Engineering Requirement`

Requirements originating from the user's task must remain distinguishable from requirements originating from regulations.

### 11. Derive acceptance criteria

Create objective acceptance criteria from:

1. the original user requirements; and
2. every material regulatory requirement identified in the Normative Basis.

Assign every acceptance criterion a stable identifier:

`AC1`, `AC2`, `AC3`, ...

Build:

`Engineering Object -> Regulatory/User Requirement -> Acceptance Criterion`

Acceptance criteria should express engineering properties that can be objectively verified.

Examples:

- all required loads are included;
- the governing load combination is selected correctly;
- design resistance is not less than design action;
- a regulatory limit is not exceeded;
- a required stability check is performed when its applicability condition is met;
- the applicable regulatory branch is derived from accepted project inputs;
- the governing airflow is selected from the calculated pollutant airflows;
- a required project input absent from the original task is explicitly identified;
- an assumed parameter remains conditional;
- user-provided values preserve their origin;
- every material regulatory requirement is traceable to its clause and proving test.

For material engineering calculations, acceptance criteria must also cover the applicable calculation-verification properties:

- input completeness and provenance;
- units;
- dimensional consistency;
- calculation method or formula basis;
- numerical substitution;
- rounding where rounding may affect compliance;
- relevant threshold or boundary cases;
- reproducibility of the reported result.

Prefer direct engineering relations over self-declared result fields.

Example:

`design_resistance >= design_action`

is stronger acceptance evidence than:

`strength_check = true`

For conditional requirements, acceptance should be derived from accepted applicability inputs rather than merely requiring an allowed result string.

### 12. Define implementation-independent compliance tests

For every acceptance criterion define how RED will later prove or disprove compliance.

The complete pre-GREEN traceability for regulatory requirements is:

`Engineering Object -> SP/SNiP/GOST Clause -> Regulatory Requirement -> Acceptance Criterion -> Compliance Test`

For user-origin requirements without a regulatory clause:

`Engineering Object -> User Requirement -> Acceptance Criterion -> Compliance Test`

One proving test may contribute evidence to multiple criteria when appropriate.

One criterion may require several tests or assertions.

Every acceptance criterion must have identifiable proving coverage.

A particular calculation method or formula should be mandatory only when:

- the regulation requires it;
- the user explicitly requires it; or
- the approved spec explicitly selects it.

Otherwise test the required engineering property rather than one arbitrary implementation.

### 13. Define engineering calculation verification

For every material numerical engineering calculation, establish enough information to make its result independently reproducible.

Where applicable define:

- accepted input values;
- input origins;
- input units;
- calculation method;
- normative or engineering basis of the method;
- formulas or algorithmic relations;
- intermediate values when required to reproduce the result;
- output units;
- rounding method;
- relevant threshold or boundary cases;
- final result.

The intended verification relation is:

`Recorded Inputs + Approved Method -> Reproducible Result`

### 14. Define the engineering output boundary

Determine the highest practical public engineering artifact representing the result.

Examples:

- calculation report;
- engineering design report;
- machine-readable calculation artifact;
- structural-model result;
- equipment selection;
- engineering decision table.

Acceptance criteria should be tested at that boundary whenever practical.

For engineering work, prefer checking the actual engineering relation rather than an internal representation.

For structural resistance, evaluate the action/resistance relation.

For governing-case selection, compare the evaluated cases.

For regulatory applicability, derive the expected branch from accepted inputs.

For ventilation calculations, compare pollutant-specific required flows and the reported governing result.

### 15. Present the spec for approval

The approval-ready engineering spec must clearly show:

- original engineering task;
- engineering objects;
- known factual inputs and their origins;
- mandatory Russian Normative Basis;
- participating SP/SNiP/GOST and other normative documents;
- relevant clauses and requirements;
- normative-source edition/status/source/verification information;
- regulatory applicability conditions;
- additional inputs discovered during specification formation;
- missing project inputs;
- proposed design assumptions;
- complete acceptance-criteria list with stable IDs;
- intended compliance-test mapping;
- RED proof;
- GREEN condition.

The user-approved version is the canonical spec for subsequent RED and GREEN work.

Acceptance criteria must describe observable behavior at the highest practical product or engineering boundary.

For backend/API work, prefer real application or public API boundaries over isolated internals. A class, method, route declaration, DTO, mock call, internal flag, requirement ID, or grep result is not acceptance evidence when the requested behavior can be tested at a practical backend/API boundary.

Example: for a public API requirement, a strong proving test sends a real HTTP/RPC request through the application boundary and asserts status/body plus required side effects. Testing only the controller or service method in isolation is not equivalent.

For engineering work, apply the same principle to the engineering result.

Example: for structural resistance, evaluate the accepted design action and resistance relation.

Example: for a conditional regulatory requirement, derive applicability from accepted project inputs or approved assumptions and verify the reported engineering decision.

When a spec file is used, commit it with an ASCII-only commit message, show this final compact canonical version to the user, and require explicit user approval before RED.

There is no `SPEC_REVIEW` stage.

### Mid-work requirement changes

If the user adds or changes a requirement after work has started, preserve the approved specification history.

Treat the working document as `SPEC-DRAFT`.

`SPEC-DRAFT` is append-only for requirement changes.

Record every new or changed requirement as:

`ADDITION: <requirement>`

For every `ADDITION`:

1. append it to `SPEC-DRAFT`;
2. record it in the task/spec change journal;
3. identify affected engineering objects, regulations, inputs, assumptions, acceptance criteria, and compliance tests;
4. commit the specification change with an ASCII-only commit message;
5. replan only the affected workflow stages;
6. update affected RED tests before relying on GREEN;
7. repeat affected RED/GREEN work and reviews as required.

If further user approval has not been waived, obtain explicit approval of the changed specification before proceeding with affected implementation work.

Do not silently erase or rewrite previously approved requirement history.

## RED

After user approval, the Implementer writes proving tests in the project's normal test location.

Every proving test must have a clear description of the behavior under test and its expected result.

**Every acceptance criterion in the approved spec must have identifiable RED proving coverage.**

Before requesting `RED_REVIEW`, the Implementer must be able to provide the complete mapping:

`Acceptance Criterion -> Proving Test -> Decisive Assertion / Expected Result`

No acceptance criterion may be silently omitted.

For engineering tasks, this includes criteria originating from:

- the original user request;
- applicable regulatory requirements;
- material calculation-verification requirements identified by the approved spec.

When a persisted spec file exists, the primary proving test should reference it, for example:

`SDDTDD SPEC: specs/spec_<number>.md`

When no persisted spec file exists, the primary proving test description must contain the complete user-approved spec, including acceptance criteria and expected result.

RED must test the approved behavior at the highest practical boundary, contain no production implementation of the requested behavior, and fail specifically because that behavior is missing or incorrect.

Syntax errors, missing dependencies, broken fixtures, environment failures, or unrelated defects are invalid RED.

For engineering work, RED uses the approved specification as the independent oracle for:

- engineering objects;
- accepted inputs;
- provenance;
- normative requirements;
- applicability branches;
- design assumptions;
- acceptance criteria;
- calculation-verification requirements.

Run the narrow proving command and commit RED with an ASCII-only commit message.

### RED_REVIEW — Reviewer agent

The independently delegated Reviewer must first read:

1. the original user request;
2. the complete approved spec;
3. the complete approved acceptance-criteria list;
4. the RED commits;
5. the proving-test evidence.

When possible, reuse the same Reviewer agent/session across repeated RED reviews for the change.

If reuse is not supported, provide the new Reviewer with previous review findings and relevant context.

The Reviewer checks that:

- RED is relevant to the approved spec and follows sound test-driven-development practice;
- tests cover **all acceptance criteria** in the approved spec;
- each proving test clearly states the behavior and expected result;
- the proving boundary is practical and sufficiently high-level;
- the observed failure is target-specific and demonstrates the requested behavior is genuinely missing or incorrect;
- RED contains no production implementation or test-only logic that manufactures success;
- test setup, environment, fixtures, and dependencies are valid enough for the RED evidence to be trusted.

For engineering tasks, the Reviewer additionally checks that:

- the approved spec contains the applicable Russian Normative Basis required by the task;
- material normative requirements are mapped to the correct document, edition, amendment status, clause, official source, and verification date;
- every material regulatory or user requirement is represented by an acceptance criterion;
- every acceptance criterion has actual proving coverage;
- additional project inputs required by regulations were identified before GREEN;
- the canonical provenance vocabulary is used consistently;
- factual inputs and assumptions remain distinguishable;
- regulatory applicability is proved from accepted inputs or approved assumptions;
- requirement origin remains separate from calculation-input origin;
- material calculation requirements have testable units, dimensional consistency, method/formula basis, rounding behavior, boundary behavior, and reproducibility where applicable;
- tests prove engineering relations rather than only self-declared status fields.

### Acceptance-criterion coverage review

The Reviewer must independently verify RED coverage criterion by criterion.

Test count alone is not evidence of complete acceptance coverage.

For every acceptance criterion determine:

- which proving test covers it;
- which assertion or observable result proves it;
- whether a materially incorrect solution would be rejected.

Before issuing the RED verdict, the Reviewer must provide an acceptance-list summary with **exactly one row for every acceptance criterion in the approved spec**:

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | `test_...` proves the requirement by asserting ... | PASS / FAIL |
| AC2 | `test_...` proves the requirement by asserting ... | PASS / FAIL |
| ... | ... | ... |

The number of rows must equal the number of acceptance criteria in the approved spec.

`RED_REVIEW: PASS` is forbidden when:

- an acceptance criterion is absent from the summary;
- an acceptance criterion has no proving test;
- the cited test does not semantically prove the criterion;
- a materially incorrect solution can satisfy the cited evidence.

Reviewer returns:

- `RED_REVIEW: PASS`
- `RED_REVIEW: FAIL`
- `RED_REVIEW: NEEDS_CLARIFICATION`
- `RED_REVIEW: BLOCKED`

On `FAIL`, the Reviewer gives concrete findings; the Implementer fixes them, commits, reruns RED, and delegates review again.

GREEN is forbidden before `RED_REVIEW: PASS`.

## GREEN

After RED review passes, the Implementer makes the minimum production or engineering change required by the approved spec and reviewed RED, using the project's existing architecture and conventions.

Avoid speculative refactors or redesign.

For engineering tasks, GREEN performs the actual approved engineering work:

- calculations;
- applicability decisions;
- engineering checks;
- selected design parameters;
- required engineering output or report.

Use the input and provenance model approved by the spec.

If a required factual project input remains missing, keep it missing unless the approved spec permits an explicit design assumption.

If an approved design assumption is used, every dependent engineering conclusion remains conditional.

For every material engineering calculation, preserve enough evidence to reproduce the result from its recorded inputs and approved method.

Run the proving tests and relevant nearby regression tests, then commit with an ASCII-only commit message.

### GREEN_REVIEW — Reviewer agent

The independently delegated Reviewer must read:

- the original user request;
- the approved spec;
- the complete acceptance-criteria list;
- the reviewed RED;
- the RED review;
- the GREEN commits;
- the engineering result.

It may run tests and inspect CI/build/test artifacts needed to verify the result.

When possible, reuse the same Reviewer agent/session across repeated RED and GREEN reviews for the change.

If reuse is not supported, provide the new Reviewer with previous review findings and relevant context.

The Reviewer checks that:

- every acceptance criterion in the approved spec has direct code/test or engineering evidence;
- reviewed RED now passes for the intended reason;
- implementation follows existing architecture and conventions;
- scope stays within the approved behavior;
- relevant regression tests pass;
- tests or spec were not weakened merely to manufacture GREEN;
- there is an explicit end-to-end trace from the original task through the approved spec and acceptance criteria to tested observable behavior and an accepted outcome that resolves that task.

For engineering tasks, the Reviewer additionally checks that:

- engineering objects and normative requirements identified in the approved spec are addressed;
- cited normative documents, editions, amendments, clauses, official sources, and verification dates support the requirements being claimed;
- applicability decisions follow from accepted factual inputs or approved assumptions;
- canonical provenance categories and states are used consistently;
- user/project inputs remain distinguishable from regulatory values and assumptions;
- design assumptions remain conditional;
- factual project data replacing an assumption causes affected calculations and applicability branches to be recomputed;
- input values match their recorded sources;
- units are correct;
- dimensions are consistent;
- calculation methods and formulas match the approved engineering or normative basis;
- numerical substitutions and material intermediate results are reproducible;
- rounding does not improperly change a compliance conclusion;
- relevant threshold and boundary cases behave correctly;
- final numerical results can be reproduced from the recorded inputs and method;
- the reported governing case is actually derived from the evaluated cases when applicable;
- final engineering conclusions follow from engineering evidence;
- the result remains traceable through:

`Original Task -> Engineering Object -> Regulation/User Requirement -> Acceptance Criterion -> Compliance Test -> Engineering Result`

Before issuing the GREEN verdict, the Reviewer must provide an acceptance-list summary with exactly one row for every acceptance criterion in the approved spec:

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | engineering/test evidence ... | PASS / FAIL |
| AC2 | engineering/test evidence ... | PASS / FAIL |
| ... | ... | ... |

The number of rows must equal the number of acceptance criteria in the approved spec.

`GREEN_REVIEW: PASS` is forbidden if any acceptance criterion is missing from the summary or lacks sufficient engineering/test evidence.

Reviewer returns:

- `GREEN_REVIEW: PASS`
- `GREEN_REVIEW: FAIL`
- `GREEN_REVIEW: NEEDS_CLARIFICATION`
- `GREEN_REVIEW: BLOCKED`

On `FAIL`, the Implementer fixes GREEN, commits, reruns tests, and delegates review again.

The workflow is complete only after `GREEN_REVIEW: PASS` and the Reviewer has explicitly confirmed that the original user task is resolved by the accepted outcome.

## Review acceptance summary

The Reviewer must include the acceptance-list summary before the RED or GREEN review verdict.

Each row must identify:

- the acceptance criterion;
- the evidence used to review it;
- its verdict.

The summary must contain one row for every acceptance criterion in the approved spec.

Passing tests never replace this criterion-by-criterion review.

## Constraints

Use the project's existing architecture and conventions.

Commit messages are ASCII-only.

Passing tests never replace independent RED/GREEN review.

For engineering work, passing tests also do not replace verification of the approved Normative Basis, regulatory applicability, input provenance, calculations, and final engineering result.

## Completion

Report:

- spec source;
- approved behavior;
- RED commit/result;
- GREEN commit/results;
- final Reviewer verdict;
- how the accepted outcome resolves the original user task.

For engineering tasks, also report:

- principal engineering objects;
- applicable Russian normative documents and relevant clauses;
- normative-source verification dates;
- important supplied inputs;
- important assumptions;
- unresolved missing inputs;
- whether engineering conclusions are final or conditional.

# Addendum — Review report examples

These examples define the minimum expected review-report structure.

## RED_REVIEW example

```text
RED_REVIEW

Acceptance-list summary:

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | `test_required_loads_are_present` verifies all loads required by the approved spec | PASS |
| AC2 | `test_governing_combination` evaluates all required combinations and verifies the reported governing case | PASS |
| AC3 | No RED test proves the required stability verification | FAIL |
| AC4 | `test_assumed_inputs_are_conditional` rejects an unsupported factual project input | PASS |

Blocking finding:

AC3 is not covered by RED.

The approved spec requires the applicable stability verification, but no proving test can reject a solution that omits it.

RED_REVIEW: FAIL
```

## GREEN_REVIEW example

```text
GREEN_REVIEW

Acceptance-list summary:

| Acceptance Criterion | How it was reviewed | Verdict |
|---|---|---|
| AC1 | All required loads are present and the reviewed RED test passes | PASS |
| AC2 | The reported governing combination matches the calculated governing effect | PASS |
| AC3 | The required stability calculation is present and satisfies the applicable regulation | PASS |
| AC4 | Assumed project inputs remain explicitly conditional in the final engineering result | PASS |

All acceptance criteria from the approved spec are covered and satisfied.

GREEN_REVIEW: PASS
```

## Engineering calculation review example

```text
Engineering calculation evidence:

Inputs:
- span = 6.0 m, user_provided
- material grade = <value>, project_provided
- design load = <value>, source recorded

Verification:
- input completeness/provenance: PASS
- units: PASS
- dimensional consistency: PASS
- calculation method/formula basis: PASS
- numerical substitution: PASS
- rounding: PASS
- relevant boundary cases: PASS
- result reproducibility: PASS
```

## Coverage rule

A review verdict must never replace the acceptance-list summary.

The summary must contain one row for every acceptance criterion in the approved spec.

Passing tests alone are not sufficient evidence.

The Reviewer must establish:

`Acceptance Criterion -> Test / Engineering Evidence -> Verdict`
