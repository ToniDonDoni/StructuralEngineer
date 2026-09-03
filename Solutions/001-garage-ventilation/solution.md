# Garage ventilation solution

## Scope and input status

This artifact proposes the ventilation and control architecture for the
360 m3 garage described in `Tasks/001-garage-ventilation/spec.md`. It does not
invent a parking-space count, location type, heating status, gate geometry,
traffic rate, outdoor temperature, vehicle data, or solvent emission data.
Those values are required project inputs and are reported as missing in
`solution.json` where they affect a conditional decision or a numerical load.

The values 2 percent entries, 8 percent exits, and 20 mg/m3 CO are preserved as
user-provided values. Clause 8.3.10 governs how the required calculation is
performed; it is not used to change the origin of these user inputs. They are
not substituted for the missing emission inventory.

## Proposed system

Use a mechanical supply-and-exhaust system with no recirculation of contaminated
exhaust air. Split the exhaust equally between the upper and lower zones. The
airflow is selected by the assimilation calculation for CO, the specified NOx
substances, and each specified solvent vapor. The design airflow remains a
calculated output and is not assigned a value until emission rates and
permissible concentrations are available.

Provide CO measurement and alarm, plus the user-required NOx/VOC or
specific-solvent monitoring. When a configured limit is exceeded, the control
system starts increased ventilation, alarm, and the user-required automatic
window and gate actions. Provide manual operation, equipment and sensor fault
indication, and protection against return of contaminated exhaust.

Fire mode has the highest priority. On a fire signal, disable general-exchange
ventilation and inhibit normal automatic opening actions while the smoke
control algorithm operates. Gates retain manual opening. Install fire dampers
where the final air-distribution design crosses applicable fire-compartment
boundaries.

## Winter operation

For a heated parking area, maintain at least 8 C during non-working hours in
accordance with clause 8.3.5. Use a heated supply-air section, temperature
control, and freeze protection. The heating-capacity calculation must include
the maximum possible hourly vehicle entries and the heat contribution of
entering vehicles in accordance with clause 8.3.8.

The current artifact does not claim a vehicle heat contribution: the entry
count, source of that count, vehicle heat model, outdoor temperature, and
parking temperature are missing project inputs. The same rule is used for the
air-thermal-curtain and redundancy decisions: the result is pending until the
exact applicability inputs are supplied.

## Pollutant calculation

For each pollutant, collect the source, emission rate, selected substance, and
permissible concentration from the applicable sanitary record. Use
assimilation under clause 8.3.10 and select the governing airflow from the
pollutant-specific calculated flows. The JSON artifact contains only
illustrative verification cases, clearly marked as such. The solvent case uses
a synthetic 50 mg/m3 comparison and is not a project limit.

The combined-effect check is mandatory where the applicable sanitary
requirements call for it. A separate illustrative case demonstrates the sum
of relative concentration terms; it must be replaced with the project values
and verified limits before final equipment sizing.

## Applicability and limits

Clause 1.2 is checked explicitly. Repair, technical maintenance, painting, and
similar technological solvent operations require a separately applicable
technology design; they are not silently covered by the ordinary parking
ventilation calculation.

`solution.json` is the acceptance artifact. It records the regulatory clauses,
user requirements, design assumptions, missing-input behavior, and the exact
traceability relation set used by the compliance tests.
