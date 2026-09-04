# Canonical Specification v0.4

## 1. Task

Develop a project solution for ventilation of a closed garage with a volume of
360 m3. The system shall:

- remove CO, NOx, and solvent vapors;
- provide the required air exchange;
- automatically control ventilation, windows, and gates using sensors;
- operate in winter without freezing the room;
- provide fire and manual control modes.

This is a design and calculation task. No numerical design result is fixed by
this specification at this stage.

The user-provided inputs that must be preserved and classified as user inputs
are:

- average number of entries: 2 percent of parking spaces;
- average number of exits: 8 percent of parking spaces;
- design CO concentration: 20 mg/m3.

These values are not to be silently converted into normative values or final
equipment selections.

## 2. Normative basis

The primary document is SP 113.13330.2023, with applicable amendments.

Relevant clauses:

- clause 1.2: applicability check;
- clause 8.3.1: heating, general-exchange, and smoke-control ventilation;
- clause 8.3.5: minimum temperature of 8 C in a heated parking facility;
- clause 8.3.8: account for heat required to warm entering vehicles;
- clause 8.3.9: air-thermal curtains at gates under specified conditions;
- clause 8.3.10: assimilation calculation of ventilation for harmful emissions;
- clause 8.3.11: fire dampers;
- clause 8.3.13: shutdown of general-exchange ventilation during a fire;
- clause 8.3.17: general-exchange supply and exhaust ventilation;
- clause 8.3.18: exhaust from upper and lower zones in equal proportions;
- clause 8.3.21: 100 percent redundancy for underground parking with more than
  25 parking spaces;
- clause 8.5.7: automation, monitoring, CO measurement, and CO alarm devices;
- clause 9.5: CO measurement and alarm devices in enclosed parking facilities;
- clause 6.1.8: manual opening of automatically operated gates.

The current status and amendment list shall be checked against the Rosstandart
record:

- https://protect.gost.ru/sp/details/c8580ef4-7e8e-4694-808f-11f5696cb131
- https://protect.gost.ru/sp/changesdetails/d9f1b091-6a91-4c03-923f-d4fe0639ef71

The requirements for harmful substances are related to GOST 12.1.005-88,
which is referenced by SP 113.13330.2023 and shall be used in its applicable
edition:

- https://protect.gost.ru/gost/details/7835f82d-eca3-444b-956f-d668fe8a4bc0

## 3. Air-exchange calculation

Air exchange shall be determined by assimilation calculation in accordance
with clause 8.3.10 of SP 113.13330.2023.

The normative input data shall be taken from the same clause. The concrete
values shall not be entered into this specification or calculated at this
stage.

For NOx and solvent vapors, the design shall identify the specific substances,
emission sources, emission rates, permissible concentrations, and any required
combined-effect check under applicable sanitary requirements.

The proving artifact shall contain explicit input records for these data and
shall distinguish user inputs, normative or project inputs, illustrative test
inputs, calculated outputs, and design assumptions. An illustrative test case
may be used to prove the governing-contaminant selection, but it shall not be
presented as the final design result.

## 4. System requirements

The design shall provide:

- supply and exhaust ventilation;
- exhaust from the upper and lower zones;
- CO sensors;
- NOx/NO2 sensors;
- VOC or specific-solvent sensors;
- automatic activation of an increased ventilation mode;
- automatic control of windows and gates;
- manual control;
- equipment and sensor fault monitoring;
- a separate fire-control algorithm;
- winter freeze protection;
- supply-air heating where required;
- no return of contaminated exhaust air to the garage.

The NOx/VOC sensors, automatic window and gate control, freeze protection,
fault monitoring, and contaminated-air return prohibition are user or design
requirements. They must not be presented as direct requirements of the cited
SP clauses unless separately supported by the applicable standards.

The design shall also explicitly evaluate the conditional requirements for
air-thermal curtains at gates, fire dampers, and 100 percent redundancy for an
underground parking facility with more than 25 parking spaces.

## 5. Applicability boundary

Clause 1.2 shall be checked explicitly. SP 113.13330.2023 does not apply to
garages where current repair or technical maintenance of vehicles is carried
out, except washing.

If solvent vapors result from repair, painting, or other technological
operations, the design shall state that SP 113.13330.2023 alone is insufficient
and that the technological zone requires a separate applicable design solution.

## 6. Acceptance criteria

The proving tests shall demonstrate that the resulting solution:

1. References clause 8.3.10 as the basis for air-exchange calculation.
2. Does not substitute unsupported design numbers for normative inputs.
3. Checks CO, NOx, and solvent vapors.
4. Determines the design flow from the governing contaminant.
5. Provides exhaust from upper and lower zones in equal proportions.
6. Provides automatic control from sensor readings.
7. Provides an emergency mode when concentrations exceed configured limits.
8. Gives the fire mode priority over general-exchange ventilation and automatic
   window/gate opening.
9. Preserves manual gate opening.
10. Checks winter temperature and freeze protection.
11. Detects missing mandatory input data.
12. Reports when clause 1.2 makes SP 113.13330.2023 inapplicable.
13. Provides supply and exhaust ventilation, general manual control, equipment
    and sensor fault monitoring, a separate fire-control algorithm, and no
    return of contaminated exhaust air.
14. Provides a traceable mapping for every relevant clause listed in Section 2,
    including a compliance-test identifier, source document, and regulatory
    requirement origin. The artifact records the amendment-status check and the
    applicable edition input for GOST 12.1.005-88.
15. Evaluates the applicability and evidence for air-thermal curtains, fire
    dampers, and underground-parking redundancy instead of silently assuming
    that each conditional requirement is or is not applicable.
16. Provides a design-report boundary with complete traceability from task
    object through requirement, acceptance criterion, and compliance test, and
    preserves the origin of each requirement or input.
17. Preserves the supplied 2 percent, 8 percent, and 20 mg/m3 values as
    user-provided inputs and contains no unsupported fixed design values.

## 7. RED proof

After explicit user approval, proving tests shall be written at the highest
practical product boundary. Before implementation they shall fail because the
calculation model and control solution are absent.

## 8. GREEN condition

All acceptance criteria shall pass. The resulting design report shall trace
each normative requirement to its SP clause and distinguish normative
requirements, user requirements, and design assumptions.
