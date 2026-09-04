# Canonical Specification v0.1

## 1. Task Summary

Determine and design a technically justified way to strengthen the existing
foundation of an old brick house without fully replacing the foundation.

The solution must retain the existing foundation as part of the final system
where technically feasible. No strengthening method or numerical design result
is fixed at the specification stage.

Original user constraint:

- strengthen the existing foundation;
- avoid complete foundation replacement.

## 2. Engineering Objects

The task includes the following material engineering objects and conditions:

- existing foundation: type, material, geometry, depth, condition, defects;
- soil base beneath and around the foundation;
- groundwater and moisture conditions;
- load-bearing brick walls and other above-ground structures affected by
  foundation deformation or load redistribution;
- current and future building loads and load paths;
- settlement, differential settlement, cracks, tilting, and other observed
  deformation indicators;
- local excavation, underpinning, temporary support, and construction sequence;
- adjacent structures, utilities, and access constraints where relevant.

## 3. Normative Basis

Normative status was checked on 2026-09-04 against official Rosstandart
records.

### Primary documents

1. **GOST 31937-2024 — Buildings and structures. Rules of inspection and
   monitoring of technical condition**, including the correction published in
   2025.
   - Relevant clauses: 5.1.4-5.1.5; 5.2.1; 5.2.10-5.2.15.
   - Role: establish the technical condition of foundations, soils, groundwater,
     defects, settlement signs, material properties, and the need for detailed
     investigation.
   - Official source:
     https://protect.gost.ru/gost/details/150801aa-be38-4abc-98d6-6f0d0aadb977

2. **SP 22.13330.2016 — Soil bases of buildings and structures**, with
   Changes 1-5.
   - Relevant clauses: 5.8.2-5.8.7; 5.8.10-5.8.15; general foundation design
     requirements of 5.1-5.7 as applicable.
   - Role: determine the need for strengthening, verify soil/foundation capacity
     and deformation, account for the condition of underground and above-ground
     structures, construction sequence, and use of the existing foundation.
   - Official source:
     https://protect.gost.ru/sp/details/71e96332-a446-4a15-87a0-2db895479f61

3. **SP 20.13330.2016 — Loads and actions**, with Changes 1-6.
   - Relevant sections: 5 and 6.
   - Role: establish loads, actions, and governing combinations for verification
     of the existing and strengthened system.
   - Official source:
     https://protect.gost.ru/sp/details/bac9e1fe-45f1-401b-8e32-949f4ee27821

### Conditional normative branches

The following documents become applicable if the selected strengthening method
or the condition of the house requires them:

4. **SP 15.13330.2020 — Masonry and reinforced masonry structures**, with
   Change 1.
   - Clause 4.5 and relevant Sections 7-9.
   - Applies when the brick superstructure requires verification or associated
     strengthening because of settlement, cracking, or load redistribution.
   - Official source:
     https://protect.gost.ru/sp/details/88d859d2-0687-4825-9d5a-004160dce187

5. **SP 427.1325800.2018 — Masonry and reinforced masonry structures. Methods
   of strengthening**, with Changes 1-2.
   - Relevant clauses: 4.1-4.2, 4.8 and Section 8.
   - Applies if masonry strengthening is required as part of the foundation
     intervention.
   - Official source:
     https://protect.gost.ru/sp/details/a9a3c500-8a9b-4155-9061-f24f6d6d01ba

6. **SP 24.13330.2021 — Pile foundations**, with Changes 1-2.
   - Relevant section: 7.6.
   - Applies if piles, micropiles, or other pile-based strengthening are selected.
   - Official source:
     https://protect.gost.ru/sp/details/1e90a34c-6379-4236-8256-38be93e29766

7. **SP 63.13330.2018 — Concrete and reinforced concrete structures. General
   provisions**, with Changes 1-2.
   - Applies if the selected solution introduces structural reinforced-concrete
     underpinning, enlargement, jackets, beams, or other reinforced-concrete
     strengthening elements.
   - Official source:
     https://protect.gost.ru/sp/details/8b67e228-0c9f-4a62-b562-964b3a58c667

8. **SP 45.13330.2017 — Earthworks, grounds and footings**, with current
   applicable changes.
   - Applies to execution and acceptance requirements for excavation,
     underpinning, soil improvement, or foundation works during reconstruction.
   - Official source:
     https://protect.gost.ru/sp/details/6b8a4ce8-2c63-46f8-8c16-6efec70cede8

## 4. Known and Missing Inputs

### Known user inputs

- the building is an old brick house;
- the existing foundation is to be strengthened;
- complete foundation replacement is excluded as the intended solution.

### Required but currently missing inputs

- project location, climatic and seismic conditions;
- building age, dimensions, number of storeys, structural layout, and known
  alterations;
- foundation type, material, width, depth, condition, and material strength;
- wall condition, crack pattern, measured settlement/tilt, and deformation
  history;
- current and planned loads;
- geotechnical profile, soil properties, bearing layers, frost/heave conditions;
- groundwater level and seasonal variation;
- drainage, waterproofing, leakage, or washout conditions;
- basement/crawlspace/access conditions and nearby utilities;
- adjacent structures that may be affected by excavation or strengthening;
- heritage or other special regulatory status, if any.

No numerical design assumption is approved at this stage. Any later
`design_assumption` must be explicit and its dependent result must remain
conditional until factual project data is available.

## 5. Acceptance Criteria

- **AC1 — Investigation basis.** The final engineering solution is based on
  sufficient inspection data to establish the technical condition of the
  foundation, soil base, groundwater conditions, and affected brick structures
  in accordance with GOST 31937-2024.

- **AC2 — Existing foundation data.** Foundation type, material, dimensions,
  depth, defects, and material condition are established from project or survey
  data, or explicitly remain missing rather than being invented.

- **AC3 — Loads.** Current and relevant future loads and governing combinations
  are established in accordance with SP 20.13330.2016 before the strengthening
  system is checked.

- **AC4 — Need and target of strengthening.** The need for strengthening and its
  required capacity/deformation target are justified from actual or projected
  foundation pressures, soil properties, settlement/deformation checks, and the
  condition of the building in accordance with SP 22.13330.2016 Section 5.8.

- **AC5 — Existing foundation retained.** The selected solution strengthens the
  existing foundation without complete replacement and uses the useful capacity
  of the existing foundation and soil base where technically justified.

- **AC6 — Alternatives considered.** Materially feasible strengthening variants
  are compared before selection, including constructive effectiveness,
  practicability, risk to the existing house, and economic reasonableness as
  required by SP 22.13330.2016 clause 5.8.14.

- **AC7 — Strength and deformation.** The selected strengthened foundation and
  soil base satisfy required strength, bearing-capacity, stability, settlement,
  and deformation checks for both construction and subsequent operation.

- **AC8 — Brick superstructure protected.** The condition and deformation
  sensitivity of the brick walls and other above-ground structures are included
  in the design, and additional settlement or load redistribution does not
  create an unacceptable structural condition.

- **AC9 — Construction sequence.** The strengthening sequence, local excavation,
  underpinning, and temporary support are defined so that stability is preserved
  during the works and uncontrolled differential settlement is avoided.

- **AC10 — Conditional method norms.** If piles/micropiles, reinforced-concrete
  strengthening, masonry strengthening, soil improvement, or another method-
  specific solution is selected, the corresponding conditional normative branch
  is identified and satisfied.

- **AC11 — Cause of distress addressed.** Where weakening is associated with
  groundwater, drainage, leakage, frost/heave, washout, or another continuing
  cause, the final solution addresses that cause rather than only increasing
  foundation section capacity.

- **AC12 — Input provenance.** User/project facts, regulatory values, calculated
  outputs, missing inputs, and any design assumptions remain distinguishable.
  Results that depend on assumptions remain explicitly conditional.

## 6. RED Proof Boundary

RED will later define proving tests for every approved acceptance criterion.
The proving boundary is the final engineering strengthening report/design
artifact, including its inspection basis, normative traceability, calculations,
selected method, construction sequence, and conditional branches.

No proving tests are defined in this specification.

## 7. GREEN Condition

GREEN is complete when the approved acceptance criteria are satisfied by a
reproducible engineering solution that selects and verifies a foundation-
strengthening method without complete replacement, using factual project data
or explicitly conditional assumptions and the applicable Russian normative
basis.
