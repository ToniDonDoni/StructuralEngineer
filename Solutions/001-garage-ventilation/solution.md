# Preliminary garage ventilation solution

## Basis

This design artifact implements `Tasks/001-garage-ventilation/spec.md` for the
360 m3 enclosed garage. The normative basis is SP 113.13330.2023 and the
applicable edition of GOST 12.1.005-88. The complete machine-readable
acceptance artifact is `solution.json` in this directory.

## System

Use a mechanical supply-and-exhaust system with no recirculation of contaminated
exhaust air. Exhaust is split equally between the upper and lower zones. Supply
air is heated as required by the winter control loop. The system includes CO,
NOx/NO2, and VOC or specific-solvent sensors.

Normal automatic control starts increased ventilation when any monitored value
exceeds its configured limit. The same sensor event commands the automatic
window and gate actuators. Equipment and sensor faults are alarmed and exposed
to the manual control mode. Automatically operated gates retain manual opening.

Fire mode has highest priority: it disables general-exchange ventilation and
prevents automatic window/gate opening while the separate smoke-control
algorithm is enabled.

## Calculation

Air exchange is determined by assimilation under clause 8.3.10. For each
pollutant, the design record contains the emission source, emission rate,
permissible-concentration source, and calculation evidence. The governing flow
is selected as the maximum of the CO, NOx, and VOC flows. The pollutant records
and illustrative verification cases are separated from final equipment
selection.

The winter heating load includes the heat contribution from entering vehicles
using the maximum possible hourly entry count and the selected vehicle
heat-balance model. The current preliminary project record uses four entries per
hour as an explicitly identified project-model input; it is not presented as a
normative value.

## Winter operation

The heated-garage minimum temperature check uses 8 C under clause 8.3.5. The
control loop starts supply-air heating and freeze protection when the measured
temperature approaches the configured low-temperature boundary.

## Conditional checks

For the preliminary project inputs recorded in `solution.json`, the garage is
heated, has external gates, is above ground, and contains 20 spaces. Therefore
the air-thermal-curtain threshold in clause 8.3.9 is not met and the curtain is
not required for this project case. The underground-parking redundancy
condition in clause 8.3.21 is also not met. Fire-damper applicability is
recorded against fire-compartment boundaries under clause 8.3.11.

Repair, technical maintenance, painting, and similar technological operations
are outside the ordinary garage applicability boundary of clause 1.2. If
solvent vapors arise from such operations, they remain in a separately
designed technology zone and require the applicable technological solution.

## Traceability

`solution.json` contains the exact clause-to-requirement-to-acceptance-test
mapping and the complete multi-row design-report traceability. User inputs,
regulatory inputs, illustrative verification inputs, calculated outputs, and
design assumptions are explicitly classified.
