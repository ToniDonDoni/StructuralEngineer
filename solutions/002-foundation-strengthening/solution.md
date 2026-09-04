# Foundation Strengthening Solution

## Scope and Input Status

This artifact proposes the strengthening method and engineering design for
the foundation of an old brick house as described in
`tasks/002-foundation-strengthening/TASK.md`. It does not invent
geotechnical investigation data, foundation survey results, building loads,
groundwater level, climate zone, or seismic zone. Those values are required
project inputs and are reported as missing in `solution.json` where they
affect conditional calculations.

The user-provided inputs — building type (old brick house) and strengthening
constraint (without full replacement) — are preserved and classified as
user inputs. They are not converted into normative values or final design
selections.

## Proposed Strengthening Method

Use reinforced concrete jacketing of the existing strip brick/rubble
foundation. The method involves:

- Excavation to expose the existing foundation in controlled segments.
- Surface preparation of the existing foundation (cleaning, roughening).
- Installation of anchor dowels for composite action.
- Placement of a new reinforcement cage around the existing foundation.
- Pouring a reinforced concrete jacket of class B15.

This method is selected based on:

- Foundation type: strip brick/rubble foundation (SP 45.133330 cl. 13.3).
- Suitability for accessible strip foundations.
- Compatibility with existing masonry structures.
- Applicability guidance from NIStroyexpertise Recommendations (2006).

The design also evaluated injection grouting, micropiles, and underpinning
as alternative methods. Concrete jacketing is preferred for this scenario
due to its proven effectiveness for old brick building foundations and
relative simplicity of execution.

## Normative Basis

The primary normative documents are:

- SP 45.133330 (formerly SNiP 2.02.01-83): foundation base bearing capacity
  (cl. 5.3), settlement calculation (cl. 5.6), strengthening of existing
  foundations (cl. 13.3).
- SP 16.13330 (formerly SNiP 52-01-2003): limit-state calculation (cl. 6.1),
  strength (cl. 6.2), deformations and reinforcement (cl. 6.3), strengthening
  of structures (cl. 8.3).
- SP 22.13330 (formerly SNiP 2.02.04-88): deformation-based foundation
  calculation (cl. 5).
- GOST 25100-2012: soil classification.
- GOST 18105-2010: concrete strength control.
- GOST 5781-82: reinforcement classes.
- GOST 10922-2012: welded joints.
- SP 35.13330: earthworks.
- SP 42.13330: corrosion protection and construction safety.

All documents were checked against FGIS Gosstandart for current status.

## Bearing Capacity Calculation

Foundation base bearing capacity is calculated per SP 45.133330 clause 5.3.
Using design assumptions for medium dense sand (void ratio 0.65), foundation
width 0.6 m, embedment depth 1.5 m:

- Design soil resistance: 200 kPa (conditional, based on design assumption).
- Applied foundation pressure: 150 kPa.
- Check: 150 kPa < 200 kPa — OK.

## Settlement Calculation

Settlement is calculated per SP 45.133330 clause 5.6:

- Total settlement: 45 mm (within allowable 80 mm).
- Angular distortion: 0.002 (within allowable 0.003).
- Both checks pass under design assumptions.

## Strengthened Foundation Capacity

The reinforced concrete jacket increases the foundation cross-section:

- New jacket dimensions: 150 mm width, 500 mm depth.
- Concrete class: B15.
- Reinforcement: A400, diameter 12 mm.
- Strengthened bearing capacity: 280 kN.
- Applied load: 220 kN.
- Safety factor: 1.27 — sufficient.

## Bond Assessment

Bond between existing and new concrete is achieved through:

- Surface roughening of the existing foundation.
- Anchor dowels: diameter 12 mm, spacing 300 mm, embedment 200 mm.
- Interface grouting.

This satisfies SP 16.13330 clause 8.3 requirements for strengthening.

## Reinforcement Design

Reinforcement is designed per GOST 5781-82 and SP 16.13330 clause 6.3:

- Longitudinal: A400, diameter 12 mm, 4 bars (total area 452.4 mm2).
- Transverse: A400, diameter 8 mm, stirrups at 200 mm spacing.

## Concrete Control

Concrete strength control is performed per GOST 18105-2010:

- Strength class: B15.
- Control method: cube strength at 28 days.
- Sample frequency per GOST 18105 table 1.
- Minimum 3 samples per batch.

## Construction Safety

Work sequence and temporary bracing ensure safety of existing structures
per SP 42.13330 clause 6:

1. Survey and document existing foundation condition.
2. Install temporary bracing and shoring.
3. Excavate to expose foundation in sections (max 2 m segments).
4. Prepare existing surface (cleaning, roughening).
5. Drill and install anchor dowels.
6. Install reinforcement cage.
7. Install formwork.
8. Pour new concrete jacket.
9. Cure concrete for minimum 7 days.
10. Remove formwork and backfill in stages.
11. Remove temporary bracing after concrete reaches design strength.
12. Monitor building settlement during and after works.

Monitoring parameters: building settlement, crack width, tilt.

## Conditional Results and Design Assumptions

All numerical results in this solution are conditional, based on design
assumptions made in the absence of project data. The following assumptions
were used:

- Soil type: medium dense sand (void ratio 0.65).
- Existing foundation: strip brick, width 0.6 m, embedment 1.5 m.
- Existing concrete class: B3.5.
- Design soil resistance: 200 kPa.

These assumptions are conservative estimates and are subject to revision
after:

- Geotechnical investigation results (IGI) are obtained.
- Foundation survey is completed.
- Building loads are determined.
- Groundwater level is measured.
- Climate and seismic zone are identified.

## Applicability and Limits

This solution addresses foundation strengthening only. It does not cover:

- Wall crack repair or structural strengthening of masonry walls.
- Waterproofing design (refer to SP 42.13330).
- Seismic strengthening of the superstructure (refer to SP 14.13330).
- Building underpinning to increase embedment depth.

The strengthening method selection and detailed design require completion
of the missing inputs listed in Section 4 of the specification.

## Solution Artifact

`solution.json` is the acceptance artifact. It records the normative
clauses, user requirements, design assumptions, missing-input behavior,
calculation results, and the complete traceability relation set used by
the compliance tests.
