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

    def test_all_requested_pollutants_are_covered(self):
        solution = load_solution()
        self.assertEqual(
            set(solution["pollutants"]), {"CO", "NOx", "solvent_vapors"}
        )

    def test_governing_airflow_is_the_maximum_pollutant_flow(self):
        solution = load_solution()
        calculation = solution["airflow_calculation"]
        self.assertEqual(
            calculation["required_flow_formula"],
            "Q_required = max(Q_CO, Q_NOx, Q_VOC)",
        )
        self.assertEqual(calculation["selection_rule"], "governing_contaminant")

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

    def test_critical_concentrations_trigger_emergency_mode(self):
        solution = load_solution()
        emergency = solution["control_logic"]["emergency_mode"]
        self.assertTrue(emergency["enabled"])
        self.assertEqual(
            emergency["trigger_condition"],
            "any_monitored_pollutant_exceeds_configured_limit",
        )
        self.assertTrue(emergency["configured_limits_required"])
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

    def test_missing_mandatory_inputs_are_reported(self):
        solution = load_solution()
        inputs = solution["inputs"]
        self.assertTrue(inputs["reject_incomplete_inputs"])
        self.assertIn("garage_type", inputs["mandatory_fields"])
        self.assertIn("solvent_emission_rates", inputs["mandatory_fields"])
        missing_input = inputs["missing_input_behavior"]
        self.assertEqual(missing_input["input_state"], "mandatory_input_absent")
        self.assertEqual(
            missing_input["result"],
            "reject_design_and_report_missing_inputs",
        )
        self.assertEqual(
            set(missing_input["reported_fields"]),
            set(inputs["mandatory_fields"]),
        )

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


if __name__ == "__main__":
    unittest.main()
