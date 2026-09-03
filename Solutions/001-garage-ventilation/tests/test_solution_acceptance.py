"""
SDDTDD SPEC: Tasks/001-garage-ventilation/spec.md

These are implementation-independent acceptance tests for the proposed
engineering solution. They evaluate the solution artifact at its public file
boundary and do not provide any production implementation.
"""

import json
import unittest
from pathlib import Path


SOLUTION_PATH = Path(__file__).parents[1] / "solution.json"

EXPECTED_USER_NUMERIC_INPUTS = {
    "average_entries_percent": 2,
    "average_exits_percent": 8,
    "design_co_concentration_mg_m3": 20,
}

EXPECTED_MANDATORY_INPUTS = {
    "garage_type",
    "garage_location_type",
    "heated_status",
    "design_outdoor_temperature",
    "design_indoor_temperature",
    "parking_space_count",
    "vehicle_entry_rate",
    "vehicle_exit_rate",
    "vehicle_emission_rates",
    "specific_nox_substances",
    "specific_solvent_substances",
    "emission_sources",
    "solvent_emission_rates",
    "permissible_concentration_sources",
    "combined_effect_check",
    "gate_and_opening_geometry",
    "fire_compartments",
    "amendment_status",
    "harmful_substance_standard_edition",
}

EXPECTED_SP_CLAUSES = {
    "1.2",
    "8.3.1",
    "8.3.5",
    "8.3.8",
    "8.3.9",
    "8.3.10",
    "8.3.11",
    "8.3.13",
    "8.3.17",
    "8.3.18",
    "8.3.21",
    "8.5.7",
    "9.5",
    "6.1.8",
}


def load_solution():
    if not SOLUTION_PATH.exists():
        raise AssertionError(
            "The proposed engineering solution artifact is missing: "
            f"{SOLUTION_PATH}"
        )
    return json.loads(SOLUTION_PATH.read_text(encoding="utf-8"))


class GarageVentilationAcceptanceTests(unittest.TestCase):
    def test_air_exchange_is_assimilation_based_and_references_clause_8_3_10(self):
        solution = load_solution()
        mapping = solution["normative_mapping"]
        requirement = next(item for item in mapping if item["clause"] == "8.3.10")
        self.assertEqual(requirement["calculation_method"], "assimilation")

    def test_no_unsupported_numeric_design_values_are_substituted(self):
        solution = load_solution()
        inputs = solution["inputs"]
        self.assertEqual(inputs["numeric_design_values"], [])
        self.assertEqual(
            inputs["numeric_values_source"],
            "SP 113.13330.2023 clause 8.3.10",
        )
        self.assertEqual(
            inputs["normative_input_sources"]["air_exchange"],
            "SP 113.13330.2023 clause 8.3.10",
        )
        user_inputs = {
            item["name"]: item for item in inputs["user_numeric_inputs"]
        }
        self.assertEqual(set(user_inputs), set(EXPECTED_USER_NUMERIC_INPUTS))
        for name, value in EXPECTED_USER_NUMERIC_INPUTS.items():
            self.assertEqual(user_inputs[name]["value"], value)
            self.assertEqual(user_inputs[name]["origin"], "user_provided")
            self.assertEqual(user_inputs[name]["design_status"], "not_a_fixed_design_value")

    def test_all_requested_pollutants_are_covered(self):
        solution = load_solution()
        self.assertEqual(
            set(solution["pollutants"]), {"CO", "NOx", "solvent_vapors"}
        )
        checks = solution["pollutant_compliance_inputs"]
        for pollutant in ("CO", "NOx", "solvent_vapors"):
            self.assertIn(pollutant, checks)
            self.assertTrue(checks[pollutant]["emission_sources_input"])
            self.assertTrue(checks[pollutant]["emission_rate_input"])
            self.assertTrue(checks[pollutant]["permissible_concentration_input"])
        for pollutant in ("NOx", "solvent_vapors"):
            self.assertTrue(checks[pollutant]["specific_substances_input"])
        combined = solution["combined_effect_check"]
        self.assertTrue(combined["required"])
        self.assertTrue(combined["input_source"])

    def test_governing_airflow_is_the_maximum_pollutant_flow(self):
        solution = load_solution()
        calculation = solution["airflow_calculation"]
        self.assertEqual(
            calculation["required_flow_formula"],
            "Q_required = max(Q_CO, Q_NOx, Q_VOC)",
        )
        self.assertEqual(calculation["selection_rule"], "governing_contaminant")
        verification = calculation["illustrative_verification_case"]
        flows = verification["pollutant_flows"]
        self.assertEqual(set(flows), {"CO", "NOx", "VOC"})
        self.assertEqual(
            verification["reported_required_flow"], max(flows.values())
        )
        self.assertEqual(
            verification["reported_governing_contaminant"],
            max(flows, key=flows.get),
        )

    def test_exhaust_is_split_equally_between_upper_and_lower_zones(self):
        solution = load_solution()
        zones = solution["ventilation_system"]["exhaust_zones"]
        self.assertEqual(zones["upper_share"], 0.5)
        self.assertEqual(zones["lower_share"], 0.5)
        self.assertEqual(zones["regulation_clause"], "8.3.18")

    def test_sensor_automation_controls_ventilation_windows_and_gates(self):
        solution = load_solution()
        control = solution["control_logic"]
        self.assertEqual(set(control["sensors"]), {"CO", "NOx", "VOC"})
        required_actions = {"ventilation", "windows", "gates"}
        self.assertTrue(required_actions.issubset(control["automatic_actions"]))
        rules = control["sensor_action_rules"]
        self.assertEqual({rule["sensor"] for rule in rules}, {"CO", "NOx", "VOC"})
        mapped_actions = set()
        for rule in rules:
            self.assertEqual(rule["condition"], "reading_exceeds_configured_limit")
            mapped_actions.update(rule["actions"])
        self.assertTrue(required_actions.issubset(mapped_actions))

    def test_section_four_requires_supply_manual_fault_and_contamination_controls(self):
        solution = load_solution()
        ventilation = solution["ventilation_system"]
        self.assertEqual(ventilation["type"], "mechanical_supply_and_exhaust")
        self.assertTrue(ventilation["manual_control"])
        self.assertTrue(ventilation["equipment_and_sensor_fault_monitoring"])
        self.assertTrue(ventilation["fire_control_algorithm"])
        self.assertTrue(ventilation["no_contaminated_exhaust_return"])
        self.assertGreaterEqual(len(ventilation["fire_algorithm_steps"]), 2)

    def test_critical_concentrations_trigger_emergency_mode(self):
        solution = load_solution()
        emergency = solution["control_logic"]["emergency_mode"]
        self.assertTrue(emergency["enabled"])
        self.assertEqual(
            emergency["trigger_condition"],
            "any_monitored_pollutant_exceeds_configured_limit",
        )
        self.assertTrue(emergency["configured_limits_required"])
        limits = emergency["configured_limits"]
        self.assertEqual(set(limits), {"CO", "NOx", "VOC"})
        for limit in limits.values():
            self.assertTrue(limit["source"])
            self.assertTrue(limit["value_input"])
        self.assertEqual(
            emergency["verification_case"]["input_state"],
            "above_configured_limit",
        )
        self.assertEqual(
            emergency["verification_case"]["expected_mode"], "emergency_mode"
        )
        self.assertIn("alarm", emergency["actions"])
        self.assertIn("maximum_exhaust", emergency["actions"])
        self.assertEqual(emergency["activation_result"], "emergency_mode")

    def test_fire_mode_has_priority_and_prevents_normal_opening(self):
        solution = load_solution()
        fire = solution["control_logic"]["fire_mode"]
        self.assertEqual(fire["priority"], "highest")
        self.assertIn("disable_general_exchange", fire["actions"])
        self.assertIn("prevent_window_gate_opening", fire["actions"])

    def test_gates_have_manual_opening(self):
        solution = load_solution()
        self.assertTrue(solution["ventilation_system"]["gates"]["manual_opening"])
        self.assertEqual(
            solution["ventilation_system"]["gates"]["regulation_clause"], "6.1.8"
        )

    def test_winter_mode_checks_temperature_heating_and_freeze_protection(self):
        solution = load_solution()
        winter = solution["winter_mode"]
        self.assertTrue(winter["freeze_protection"])
        self.assertTrue(winter["heating_capacity_check"])
        self.assertIn("8.3.5", winter["regulation_clauses"])
        self.assertIn("8.3.8", winter["regulation_clauses"])
        temperature_check = winter["temperature_check"]
        self.assertEqual(temperature_check["heated_parking_minimum_c"], 8)
        self.assertEqual(temperature_check["source_clause"], "8.3.5")
        self.assertEqual(temperature_check["unheated_setpoint"], "project_input")
        self.assertEqual(
            temperature_check["low_temperature_response"],
            "enable_heating_and_protect_against_freezing",
        )
        entering_vehicle = winter["entering_vehicle_heat_load"]
        self.assertTrue(entering_vehicle["required_inputs"])
        self.assertTrue(entering_vehicle["calculation_check"])
        self.assertEqual(entering_vehicle["regulation_clause"], "8.3.8")

    def test_missing_mandatory_inputs_are_reported(self):
        solution = load_solution()
        inputs = solution["inputs"]
        self.assertTrue(inputs["reject_incomplete_inputs"])
        self.assertTrue(EXPECTED_MANDATORY_INPUTS.issubset(inputs["mandatory_fields"]))
        missing_input = inputs["missing_input_behavior"]
        self.assertEqual(missing_input["input_state"], "mandatory_input_absent")
        self.assertEqual(
            missing_input["result"],
            "reject_design_and_report_missing_inputs",
        )
        self.assertTrue(EXPECTED_MANDATORY_INPUTS.issubset(missing_input["reported_fields"]))

    def test_applicability_check_uses_clause_1_2(self):
        solution = load_solution()
        applicability = solution["applicability"]
        self.assertEqual(applicability["regulation_clause"], "1.2")
        self.assertIn("repair", applicability["excluded_activities"])
        self.assertIn("technical_maintenance", applicability["excluded_activities"])
        self.assertTrue(applicability["separate_technology_zone_required"])
        self.assertEqual(
            applicability["decisions"]["repair_or_technical_maintenance_present"],
            "inapplicable_under_clause_1.2",
        )
        self.assertEqual(
            applicability["decisions"]["solvent_technology_present"],
            "separate_technology_zone_required",
        )

    def test_normative_requirements_have_traceable_compliance_evidence(self):
        solution = load_solution()
        mapping = {item["clause"]: item for item in solution["normative_mapping"]}
        self.assertTrue(EXPECTED_SP_CLAUSES.issubset(mapping))
        for clause in EXPECTED_SP_CLAUSES:
            self.assertEqual(mapping[clause]["source_document"], "SP 113.13330.2023")
            self.assertTrue(mapping[clause]["compliance_test_id"])
            self.assertEqual(mapping[clause]["requirement_origin"], "regulatory")
        references = solution["normative_references"]
        self.assertTrue(references["amendment_status_check"])
        self.assertEqual(references["harmful_substance_standard"], "GOST 12.1.005-88")
        self.assertTrue(references["harmful_substance_standard_edition_input"])

    def test_conditional_gate_fire_and_redundancy_requirements_are_evaluated(self):
        solution = load_solution()
        gate = solution["conditional_design_checks"]["air_thermal_curtain"]
        self.assertTrue(gate["conditional"])
        self.assertTrue(gate["applicability_inputs"])
        self.assertEqual(gate["decision"], "conditional_project_check")

        dampers = solution["conditional_design_checks"]["fire_dampers"]
        self.assertTrue(dampers["required"])
        self.assertTrue(dampers["evidence"])
        self.assertEqual(dampers["regulation_clause"], "8.3.11")

        redundancy = solution["conditional_design_checks"]["redundancy"]
        self.assertEqual(
            redundancy["condition"], "underground_parking_more_than_25_spaces"
        )
        self.assertEqual(redundancy["requirement_if_condition"], "100_percent_reserve")
        self.assertEqual(redundancy["decision"], "conditional_project_check")

    def test_design_report_preserves_requirement_origins_and_complete_traceability(self):
        solution = load_solution()
        report = solution["design_report"]
        self.assertEqual(report["path"], "Solutions/001-garage-ventilation/solution.md")
        self.assertTrue(report["traceability_complete"])
        self.assertTrue(report["required_sections"])
        traceability = solution["traceability"]
        self.assertTrue(traceability)
        origins = {item["origin"] for item in traceability}
        self.assertTrue({"regulatory", "user", "design_assumption"}.issubset(origins))
        for item in traceability:
            self.assertTrue(item["compliance_test_id"])


if __name__ == "__main__":
    unittest.main()
