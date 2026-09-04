# Canonical Specification

## 1. Task Summary

Strengthen the foundation of an existing old brick house without full
replacement. The solution shall select a strengthening method, perform
bearing-capacity and settlement calculations, design the strengthening
construction, and prepare project documentation.

This is a design-and-calculation task. No numerical design result is fixed
by this specification at this stage.

The user-provided inputs that must be preserved and classified as user
inputs are:

- building type: old brick house;
- strengthening constraint: without full replacement of the foundation.

These values are not to be silently converted into normative values or
final design selections.

## 2. Engineering Objects

- Existing foundation: strip brick or rubble foundation of the old building.
- Foundation soil (base): ground support beneath the foundation base.
- Brick masonry walls: structural elements transferring loads to the
  foundation.
- Existing and new materials: brick, concrete, reinforcing steel — for
  composite action assessment.
- Building loads: dead weight of structures, live and operational loads.
- Groundwater: level and seasonal fluctuations — effect on design soil
  resistance.
- Seismic zoning: seismicity of the construction site.
- Construction conditions: possibility of work without stopping building
  operation.

## 3. Normative Basis

SP 45.133330 (formerly SNiP 2.02.01-83) "Earth bases, foundations and
structures", current edition, Note 1 (2024):

- clause 5.3: foundation base bearing capacity calculation;
- clause 5.6: settlement calculation;
- clause 13.3: strengthening of existing building foundations;
- Annex D: foundation surveys.

SP 16.13330 (formerly SNiP 52-01-2003) "Concrete and reinforced concrete
structures", current edition (2012 with amendments):

- clause 6.1: limit-state calculation;
- clause 6.2: strength;
- clause 6.3: deformations;
- clause 8.3: strengthening of structures.

SP 22.13330 (formerly SNiP 2.02.04-88) "Foundations of buildings and
structures", current edition (2016 with amendments):

- clause 5: deformation-based foundation calculation;
- clause 6: settlements.

GOST 25100-2012 "Soils. Classification", sections 4-7.

GOST 18105-2010 "Concrete. Rules for control and strength assessment".

GOST 5781-82 "Hot-rolled steel for reinforcement".

GOST 10922-2012 "Welded joints of reinforced and prestressed structures".

GOST 31996-2012 "Concrete mixes".

SP 35.13330 (formerly SNiP 2.06.15-85) "Engineering preparation of
territories", clause 6: earthworks.

SP 42.13330 (formerly SNiP 3.01.04-87) "Corrosion protection", clause 6:
underground structure protection.

NIStroyexpertise Recommendations "Typical technical solutions for
strengthening foundations of brick buildings" (2006): methods — concrete
jacketing, injection, micropiles.

Verification sources:

- FGIS Gosstandart (fgis.gost.ru) — document status.
- Minstroy RF (minstroyrf.gov.ru/docs/) — normative catalogue.

## 4. Known Inputs

| Parameter | Value | Origin |
|---|---|---|
| Building type | Old brick house | user_provided |
| Strengthening constraint | Without full foundation replacement | user_provided |
| Geotechnical investigation results (IGI) | Not available | missing |
| Foundation survey results | Not available | missing |
| Building loads | Not determined | missing |
| Groundwater level | Not determined | missing |
| Climate zone | Not determined | missing |
| Seismic zone | Not determined | missing |

## 5. Missing Inputs and Assumptions

All project data is absent. The following are required:

- Geotechnical investigation results (IGI): soil type, state, strength
  and deformation characteristics, groundwater level.
- Existing foundation survey: type (strip, column, etc.), material,
  cross-section dimensions, embedment depth, concrete or masonry strength,
  damage presence.
- Calculated building loads (dead weight of structures, live loads).
- Masonry wall survey results.
- Building deformation data (cracks, tilts, inclination).
- Climate and seismic zone.

Design assumptions may be introduced later to perform conditional
calculations when specific inputs remain missing. All results obtained
using design assumptions are conditional and subject to revision after
the missing inputs are obtained and during RED review.

## 6. Acceptance Criteria

The proving tests shall demonstrate that the resulting solution:

1. Selects the strengthening method based on foundation type, foundation
   soil characteristics, and survey results (SP 45.133330 cl. 13.3;
   NIStroyexpertise Recommendations).
2. Calculates foundation base bearing capacity in accordance with clause
   5.3 of SP 45.133330.
3. Calculates settlement in accordance with clause 5.6 of SP 45.133330
   and verifies it does not exceed allowable values.
4. Ensures bearing capacity of the strengthened foundation is greater than
   or equal to the calculated building load (SP 16.13330 cl. 6.1-6.2).
5. Verifies that foundation base pressure does not exceed the design soil
   resistance (SP 45.133330 cl. 5.3).
6. Ensures bond between existing and new concrete is achieved through
   interlocking, roughness, or anchors (SP 16.13330 cl. 8.3;
   NIStroyexpertise Recommendations).
7. Designs reinforcement of the strengthening in accordance with
   GOST 5781-82 and SP 16.13330 clause 6.3.
8. Controls concrete strength of the strengthening in accordance with
   GOST 18105-2010.
9. Specifies work sequence and temporary bracing to ensure safety of
   existing structures during construction (SP 42.13330).
10. Performs all required checks: base bearing capacity, foundation
    bearing capacity, settlement, bond, reinforcement.
11. Ensures calculation results are reproducible and contain a complete
    chain: input data, method, calculation, result.
12. Reflects every normative reference from Section 3 in the calculation
    results with clause number and check identification.
