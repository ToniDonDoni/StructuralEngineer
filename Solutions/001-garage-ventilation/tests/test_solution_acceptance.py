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
    "garage_volume_m3": 360,
    "average_entries_percent": 2,
    "average_exits_percent": 8,
    "design_co_concentration_mg_m3": 20,
}

EXPECTED_MANDATORY_INPUTS = {
    "garage_volume_m3",
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

EXPECTED_TRACEABILITY = {
    ("air_exchange_calculation", "8.3.10", "assimilation_calculation_for_harmful_emissions", "AC1", "test_air_exchange_is_assimilation_based_and_references_clause_8_3_10"),
    ("numeric_input_classification", "user", "numeric_input_classification", "AC2", "test_no_unsupported_numeric_design_values_are_substituted"),
    ("pollutant_compliance", "8.3.10", "assimilation_calculation_for_harmful_emissions", "AC3", "test_all_requested_pollutants_are_covered"),
    ("governing_airflow", "8.3.10", "assimilation_calculation_for_harmful_emissions", "AC4", "test_governing_airflow_is_the_maximum_pollutant_flow"),
    ("exhaust_zones", "8.3.18", "equal_upper_and_lower_exhaust_zones", "AC5", "test_exhaust_is_split_equally_between_upper_and_lower_zones"),
    ("co_monitoring", "8.5.7", "automation_monitoring_co_measurement_and_alarm", "AC6", "test_sensor_automation_controls_ventilation_windows_and_gates"),
    ("emergency_mode", "8.5.7", "automation_monitoring_co_measurement_and_alarm", "AC7", "test_critical_concentrations_trigger_emergency_mode"),
    ("co_monitoring", "9.5", "co_measurement_and_alarm_in_enclosed_parking", "AC6", "test_sensor_automation_controls_ventilation_windows_and_gates"),
    ("fire_mode", "8.3.13", "fire_shutdown_of_general_exchange_ventilation", "AC8", "test_fire_mode_has_priority_and_prevents_normal_opening"),
    ("manual_gate_opening", "6.1.8", "manual_gate_opening", "AC9", "test_gates_have_manual_opening"),
    ("winter_operation", "8.3.5", "heated_parking_minimum_temperature", "AC10", "test_winter_mode_checks_temperature_heating_and_freeze_protection"),
    ("winter_operation", "8.3.8", "entering_vehicle_heat_load", "AC10", "test_winter_mode_checks_temperature_heating_and_freeze_protection"),
    ("mandatory_inputs", "8.3.10", "assimilation_calculation_for_harmful_emissions", "AC11", "test_missing_mandatory_inputs_are_reported"),
    ("applicability_boundary", "1.2", "applicability_boundary", "AC12", "test_applicability_check_uses_clause_1_2"),
    ("ventilation_safety_controls", "8.3.1", "heating_general_exchange_and_smoke_control_ventilation", "AC13", "test_section_four_requires_supply_manual_fault_and_contamination_controls"),
    ("ventilation_safety_controls", "8.3.17", "general_exchange_supply_and_exhaust", "AC13", "test_section_four_requires_supply_manual_fault_and_contamination_controls"),
    ("additional_pollutant_sensors", "user", "NOx_VOC_sensor_monitoring", "AC6", "test_sensor_automation_controls_ventilation_windows_and_gates"),
    ("automatic_openings", "user", "automatic_window_gate_control", "AC6", "test_sensor_automation_controls_ventilation_windows_and_gates"),
    ("manual_fault_safety", "user", "manual_fault_and_contamination_controls", "AC13", "test_section_four_requires_supply_manual_fault_and_contamination_controls"),
    ("normative_traceability", "user", "normative_traceability", "AC14", "test_normative_requirements_have_traceable_compliance_evidence"),
    ("conditional_requirements", "8.3.9", "conditional_air_thermal_curtain", "AC15", "test_conditional_gate_fire_and_redundancy_requirements_are_evaluated"),
    ("conditional_requirements", "8.3.11", "conditional_fire_dampers", "AC15", "test_conditional_gate_fire_and_redundancy_requirements_are_evaluated"),
    ("conditional_requirements", "8.3.21", "conditional_100_percent_redundancy", "AC15", "test_conditional_gate_fire_and_redundancy_requirements_are_evaluated"),
    ("design_report_traceability", "user", "complete_engineering_task_traceability", "AC16", "test_design_report_preserves_requirement_origins_and_complete_traceability"),
    ("user_numeric_inputs", "user", "user_provided_numeric_inputs", "AC17", "test_no_unsupported_numeric_design_values_are_substituted"),
}

EXPECTED_TRACEABILITY_ORIGINS = {
    row: "user" if row[1] == "user" else "regulatory"
    for row in EXPECTED_TRACEABILITY
}

EXPECTED_CLAUSE_REQUIREMENTS = {
    "1.2": "applicability_boundary",
    "8.3.1": "heating_general_exchange_and_smoke_control_ventilation",
    "8.3.5": "heated_parking_minimum_temperature",
    "8.3.8": "entering_vehicle_heat_load",
    "8.3.9": "conditional_air_thermal_curtain",
    "8.3.10": "assimilation_calculation_for_harmful_emissions",
    "8.3.11": "conditional_fire_dampers",
    "8.3.13": "fire_shutdown_of_general_exchange_ventilation",
    "8.3.17": "general_exchange_supply_and_exhaust",
    "8.3.18": "equal_upper_and_lower_exhaust_zones",
    "8.3.21": "conditional_100_percent_redundancy",
    "8.5.7": "automation_monitoring_co_measurement_and_alarm",
    "9.5": "co_measurement_and_alarm_in_enclosed_parking",
    "6.1.8": "manual_gate_opening",
}

EXPECTED_AMENDMENTS = {"1", "2", "3"}

EXPECTED_GOST_EDITION = (
    "GOST 12.1.005-88 active edition; registry status verified on 2026-09-03"
)

EXPECTED_NUMERIC_CONTEXTS = {
    "/inputs/user_numeric_inputs/0/value": ("user_provided", "user_provided", 360),
    "/inputs/user_numeric_inputs/1/value": ("user_provided", "user_provided", 2),
    "/inputs/user_numeric_inputs/2/value": ("user_provided", "user_provided", 8),
    "/inputs/user_numeric_inputs/3/value": ("user_provided", "user_provided", 20),
    "/inputs/vehicle_entry_rate/value": ("user_provided", "user_provided", 2),
    "/inputs/vehicle_exit_rate/value": ("user_provided", "user_provided", 8),
    "/combined_effect_check/illustrative_verification_case/relative_concentration_terms/CO": ("illustrative_verification_input", "illustrative_verification_input", 0.5),
    "/combined_effect_check/illustrative_verification_case/relative_concentration_terms/NOx": ("illustrative_verification_input", "illustrative_verification_input", 0.25),
    "/combined_effect_check/illustrative_verification_case/relative_concentration_terms/solvent_vapors": ("illustrative_verification_input", "illustrative_verification_input", 0.1),
    "/combined_effect_check/illustrative_verification_case/reported_sum": ("calculated_output", "calculated_output", 0.85),
    "/pollutant_compliance_results/CO/illustrative_evaluation_case/reported_concentration": ("illustrative_verification_input", "illustrative_verification_input", 10),
    "/pollutant_compliance_results/CO/illustrative_evaluation_case/permissible_concentration": ("illustrative_verification_input", "illustrative_verification_input", 20),
    "/pollutant_compliance_results/NOx/illustrative_evaluation_case/reported_concentration": ("illustrative_verification_input", "illustrative_verification_input", 1),
    "/pollutant_compliance_results/NOx/illustrative_evaluation_case/permissible_concentration": ("illustrative_verification_input", "illustrative_verification_input", 2),
    "/pollutant_compliance_results/solvent_vapors/illustrative_evaluation_case/reported_concentration": ("illustrative_verification_input", "illustrative_verification_input", 1),
    "/pollutant_compliance_results/solvent_vapors/illustrative_evaluation_case/permissible_concentration": ("illustrative_verification_input", "illustrative_verification_input", 50),
    "/airflow_calculation/illustrative_verification_case/pollutant_flows/CO": ("illustrative_verification_input", "illustrative_verification_input", 100),
    "/airflow_calculation/illustrative_verification_case/pollutant_flows/NOx": ("illustrative_verification_input", "illustrative_verification_input", 200),
    "/airflow_calculation/illustrative_verification_case/pollutant_flows/VOC": ("illustrative_verification_input", "illustrative_verification_input", 150),
    "/airflow_calculation/illustrative_verification_case/reported_required_flow": ("calculated_output", "calculated_output", 200),
    "/ventilation_system/exhaust_zones/upper_share": ("normative_or_project_input", "normative_or_project_input", 0.5),
    "/ventilation_system/exhaust_zones/lower_share": ("normative_or_project_input", "normative_or_project_input", 0.5),
    "/control_logic/emergency_mode/verification_case/sensor_readings/CO": ("illustrative_verification_input", "illustrative_verification_input", 21),
    "/control_logic/emergency_mode/verification_case/sensor_readings/NOx": ("illustrative_verification_input", "illustrative_verification_input", 3),
    "/control_logic/emergency_mode/verification_case/sensor_readings/VOC": ("illustrative_verification_input", "illustrative_verification_input", 3),
    "/control_logic/emergency_mode/verification_case/threshold_values/CO": ("illustrative_verification_input", "illustrative_verification_input", 20),
    "/control_logic/emergency_mode/verification_case/threshold_values/NOx": ("illustrative_verification_input", "illustrative_verification_input", 2),
    "/control_logic/emergency_mode/verification_case/threshold_values/VOC": ("illustrative_verification_input", "illustrative_verification_input", 2),
    "/winter_mode/temperature_check/heated_parking_minimum_c": ("normative_or_project_input", "normative_or_project_input", 8),
}

PROJECT_INPUT_NUMERIC_PATHS = {
    "/inputs/parking_space_count/value",
    "/inputs/maximum_possible_hourly_entry_count/value",
    "/inputs/outdoor_temperature/value",
    "/inputs/parking_temperature/value",
}

TRACEABLE_PROJECT_ORIGINS = {
    "user_provided",
    "normative_or_project_input",
    "design_assumption",
}
TRACEABLE_PROJECT_STATUSES = {
    "current_project_input",
    "conditional_assumption",
}

EXPECTED_CLAUSE_TESTS = {
    "1.2": "test_applicability_check_uses_clause_1_2",
    "8.3.1": "test_section_four_requires_supply_manual_fault_and_contamination_controls",
    "8.3.5": "test_winter_mode_checks_temperature_heating_and_freeze_protection",
    "8.3.8": "test_winter_mode_checks_temperature_heating_and_freeze_protection",
    "8.3.9": "test_conditional_gate_fire_and_redundancy_requirements_are_evaluated",
    "8.3.10": "test_air_exchange_is_assimilation_based_and_references_clause_8_3_10",
    "8.3.11": "test_conditional_gate_fire_and_redundancy_requirements_are_evaluated",
    "8.3.13": "test_fire_mode_has_priority_and_prevents_normal_opening",
    "8.3.17": "test_section_four_requires_supply_manual_fault_and_contamination_controls",
    "8.3.18": "test_exhaust_is_split_equally_between_upper_and_lower_zones",
    "8.3.21": "test_conditional_gate_fire_and_redundancy_requirements_are_evaluated",
    "8.5.7": "test_sensor_automation_controls_ventilation_windows_and_gates",
    "9.5": "test_sensor_automation_controls_ventilation_windows_and_gates",
    "6.1.8": "test_gates_have_manual_opening",
}

EXPECTED_CLAUSE_ACCEPTANCE = {
    "1.2": "AC12",
    "8.3.1": "AC13",
    "8.3.5": "AC10",
    "8.3.8": "AC10",
    "8.3.9": "AC15",
    "8.3.10": "AC1",
    "8.3.11": "AC15",
    "8.3.13": "AC8",
    "8.3.17": "AC13",
    "8.3.18": "AC5",
    "8.3.21": "AC15",
    "8.5.7": "AC6",
    "9.5": "AC6",
    "6.1.8": "AC9",
}

EXPECTED_TEST_IDS = {row[-1] for row in EXPECTED_TRACEABILITY}

AIR_CURTAIN_PROJECT_INPUTS = {
    "heated_status",
    "parking_space_count",
    "external_entry_exit_gates_present",
}

REDUNDANCY_PROJECT_INPUTS = {
    "garage_location_type",
    "parking_space_count",
}

FIRE_DAMPER_PROJECT_INPUTS = {
    "fire_compartments",
    "ventilation_crosses_fire_compartment_boundaries",
}

ENTERING_VEHICLE_HEAT_PROJECT_INPUTS = {
    "maximum_possible_hourly_entry_count",
    "maximum_possible_hourly_entry_count_source",
    "vehicle_heat_load_model",
    "outdoor_temperature",
    "parking_temperature",
}


def available_project_inputs(inputs, required_names):
    """Return project inputs that are present and have a usable value."""
    def usable(value):
        if not isinstance(value, dict):
            return False
        if not {"value", "origin", "source", "status"}.issubset(value):
            return False
        if value["value"] in (None, "", {}):
            return False
        if value["origin"] not in TRACEABLE_PROJECT_ORIGINS:
            return False
        if not isinstance(value["source"], str) or not value["source"].strip():
            return False
        if value["status"] not in TRACEABLE_PROJECT_STATUSES:
            return False
        if value["origin"] == "design_assumption":
            return (
                value["status"] == "conditional_assumption"
                and isinstance(value.get("scenario_intent"), str)
                and bool(value["scenario_intent"].strip())
            )
        return value["status"] == "current_project_input"

    return {
        name: inputs[name]
        for name in required_names
        if name in inputs and usable(inputs[name])
    }


def iter_numeric_values(value, path=()):
    """Yield JSON-pointer paths for numeric values outside the registry."""
    if path and path[0] == "numeric_value_registry":
        return
    if isinstance(value, bool):
        return
    if isinstance(value, (int, float)):
        yield "/" + "/".join(str(part) for part in path), value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from iter_numeric_values(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_numeric_values(child, path + (index,))


def json_pointer_value(value, pointer):
    current = value
    for part in pointer.strip("/").split("/"):
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current


def input_value(inputs, name):
    value = inputs[name]
    return value["value"] if isinstance(value, dict) and "value" in value else value


def contains_design_assumption(records):
    return any(
        isinstance(record, dict) and record.get("origin") == "design_assumption"
        for record in records.values()
    )


def assert_assumption_intent(test_case, record, marker):
    if record.get("origin") == "design_assumption":
        test_case.assertEqual(record["status"], "conditional_assumption")
        test_case.assertIn(marker, record["scenario_intent"])


def available_mandatory_inputs(inputs):
    placeholder_fields = {
        "vehicle_emission_rates",
        "solvent_emission_rates",
        "gate_and_opening_geometry",
        "fire_compartments",
    }
    def present(value):
        if value in (None, "", {}):
            return False
        if isinstance(value, dict) and "value" in value:
            return value["value"] not in (None, "", {})
        return True

    available = {
        name: inputs[name]
        for name in EXPECTED_MANDATORY_INPUTS
        if name in inputs
        and name not in placeholder_fields
        and present(inputs[name])
    }
    user_names = {
        item["name"]
        for item in inputs.get("user_numeric_inputs", [])
        if item.get("origin") == "user_provided"
        and item.get("source") == "original_task_user_input"
    }
    if "garage_volume_m3" in user_names:
        available["garage_volume_m3"] = "user_numeric_inputs"
    return available


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
            self.assertEqual(user_inputs[name]["source"], "original_task_user_input")
            self.assertNotIn("normative_basis", user_inputs[name])
        categories = inputs["numeric_value_categories"]
        self.assertTrue(
            {
                "user_provided",
                "normative_or_project_input",
                "illustrative_verification_input",
                "calculated_output",
                "design_assumption",
            }.issubset(categories)
        )
        values = dict(iter_numeric_values(solution))
        registry = {
            item["json_pointer"]: item
            for item in solution["numeric_value_registry"]
        }
        self.assertEqual(set(registry), set(values))
        self.assertTrue(set(values).issubset(
            set(EXPECTED_NUMERIC_CONTEXTS) | PROJECT_INPUT_NUMERIC_PATHS
        ))
        for pointer, value in values.items():
            entry = registry[pointer]
            self.assertEqual(entry["value"], value)
            if pointer in EXPECTED_NUMERIC_CONTEXTS:
                expected_origin, expected_classification, expected_value = (
                    EXPECTED_NUMERIC_CONTEXTS[pointer]
                )
                self.assertEqual(value, expected_value)
                self.assertEqual(entry["origin"], expected_origin)
                self.assertEqual(entry["classification"], expected_classification)
            else:
                self.assertIn(pointer, PROJECT_INPUT_NUMERIC_PATHS)
                record = json_pointer_value(
                    solution, pointer.rsplit("/", 1)[0]
                )
                self.assertIsInstance(record, dict)
                self.assertIn(record["origin"], TRACEABLE_PROJECT_ORIGINS)
                self.assertTrue(record["source"])
                self.assertIn(record["status"], TRACEABLE_PROJECT_STATUSES)
                if record["origin"] == "design_assumption":
                    self.assertEqual(record["status"], "conditional_assumption")
                    self.assertTrue(record.get("scenario_intent"))
                    expected_classification = "design_assumption"
                else:
                    self.assertEqual(record["status"], "current_project_input")
                    expected_classification = "normative_or_project_input"
                self.assertEqual(entry["origin"], record["origin"])
                self.assertEqual(entry["classification"], expected_classification)

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
        combined_case = combined["illustrative_verification_case"]
        self.assertEqual(
            combined_case["origin"], "illustrative_verification_input"
        )
        self.assertEqual(
            set(combined_case["relative_concentration_terms"]),
            {"CO", "NOx", "solvent_vapors"},
        )
        self.assertAlmostEqual(
            combined_case["reported_sum"],
            sum(combined_case["relative_concentration_terms"].values()),
        )
        self.assertLessEqual(combined_case["reported_sum"], 1)
        self.assertEqual(combined_case["reported_status"], "within_combined_limit")
        self.assertTrue(combined_case["evidence"])
        results = solution["pollutant_compliance_results"]
        self.assertEqual(set(results), {"CO", "NOx", "solvent_vapors"})
        for pollutant in ("CO", "NOx", "solvent_vapors"):
            result = results[pollutant]
            self.assertEqual(result["pollutant"], pollutant)
            self.assertEqual(result["calculation_method"], "assimilation")
            case = result["illustrative_evaluation_case"]
            self.assertEqual(case["origin"], "illustrative_verification_input")
            self.assertLessEqual(
                case["reported_concentration"], case["permissible_concentration"]
            )
            self.assertEqual(case["reported_status"], "within_limit")
            self.assertTrue(result["evidence"])

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
        fire_algorithm = ventilation["fire_algorithm_evidence"]
        self.assertEqual(fire_algorithm["input_state"], "fire_signal")
        self.assertEqual(
            fire_algorithm["normal_mode_state"], "general_exchange_enabled"
        )
        self.assertEqual(
            fire_algorithm["fire_mode_result"],
            "general_exchange_disabled_and_smoke_control_enabled",
        )
        self.assertEqual(
            set(fire_algorithm["evidence_clauses"]), {"8.3.1", "8.3.13"}
        )

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
        verification = emergency["verification_case"]
        self.assertEqual(verification["origin"], "illustrative_verification_input")
        readings = verification["sensor_readings"]
        thresholds = verification["threshold_values"]
        self.assertEqual(set(readings), {"CO", "NOx", "VOC"})
        self.assertEqual(set(thresholds), {"CO", "NOx", "VOC"})
        exceeded = {
            pollutant
            for pollutant in readings
            if readings[pollutant] > thresholds[pollutant]
        }
        self.assertTrue(exceeded)
        self.assertEqual(set(verification["exceeded_pollutants"]), exceeded)
        self.assertEqual(verification["input_state"], "above_configured_limit")
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
        self.assertEqual(
            set(entering_vehicle["required_inputs"]),
            ENTERING_VEHICLE_HEAT_PROJECT_INPUTS,
        )
        inputs = solution["inputs"]
        available_inputs = available_project_inputs(
            inputs, ENTERING_VEHICLE_HEAT_PROJECT_INPUTS
        )
        missing_inputs = ENTERING_VEHICLE_HEAT_PROJECT_INPUTS - set(available_inputs)
        self.assertIn(
            entering_vehicle["project_input_state"],
            {"checked", "pending_missing_input"},
        )
        if missing_inputs:
            self.assertEqual(
                entering_vehicle["project_input_state"], "pending_missing_input"
            )
            self.assertEqual(
                set(entering_vehicle["missing_project_inputs"]), missing_inputs
            )
        else:
            self.assertEqual(entering_vehicle["project_input_state"], "checked")
            assumption_markers = {
                "maximum_possible_hourly_entry_count": "maximum_hourly_entries",
                "maximum_possible_hourly_entry_count_source": "maximum_hourly_entries",
                "vehicle_heat_load_model": "vehicle_heat_model",
                "outdoor_temperature": "temperature",
                "parking_temperature": "temperature",
            }
            for name, marker in assumption_markers.items():
                assert_assumption_intent(
                    self, inputs[name], marker
                )
            heat_case = entering_vehicle["current_project_case"]
            has_assumption = contains_design_assumption(
                {
                    name: inputs[name]
                    for name in ENTERING_VEHICLE_HEAT_PROJECT_INPUTS
                }
            )
            expected_heat_origin = (
                "conditional_design_assumption"
                if has_assumption
                else "current_project_inputs"
            )
            self.assertEqual(heat_case["origin"], expected_heat_origin)
            self.assertEqual(
                heat_case["entry_count_basis"],
                "maximum_possible_hourly_entry_count",
            )
            self.assertEqual(
                heat_case["maximum_possible_hourly_entry_count"],
                input_value(inputs, "maximum_possible_hourly_entry_count"),
            )
            self.assertGreater(
                heat_case["maximum_possible_hourly_entry_count"], 0
            )
            self.assertEqual(
                heat_case["maximum_possible_hourly_entry_count_source"],
                input_value(inputs, "maximum_possible_hourly_entry_count_source"),
            )
            contribution = heat_case["entering_vehicle_heat_contribution"]
            self.assertEqual(
                contribution["model"], input_value(inputs, "vehicle_heat_load_model")
            )
            self.assertEqual(
                set(contribution["input_references"]),
                ENTERING_VEHICLE_HEAT_PROJECT_INPUTS,
            )
            self.assertIsInstance(contribution["result"], (int, float))
            self.assertGreater(contribution["result"], 0)
            self.assertEqual(contribution["units"], "W")
            evidence = contribution["evidence"]
            self.assertIsInstance(evidence, dict)
            self.assertTrue(evidence["calculation_method"])
            self.assertTrue(evidence["source"])
            self.assertTrue(evidence["input_values"])
            self.assertTrue(evidence["result_record"])
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
        available = available_mandatory_inputs(inputs)
        expected_missing = EXPECTED_MANDATORY_INPUTS - set(available)
        self.assertEqual(
            set(missing_input["reported_fields"]), expected_missing
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
            self.assertEqual(
                mapping[clause]["requirement"], EXPECTED_CLAUSE_REQUIREMENTS[clause]
            )
            self.assertEqual(
                mapping[clause]["acceptance_criterion"],
                EXPECTED_CLAUSE_ACCEPTANCE[clause],
            )
            self.assertEqual(
                mapping[clause]["compliance_test_id"], EXPECTED_CLAUSE_TESTS[clause]
            )
            self.assertEqual(
                mapping[clause]["evidence"]["test_id"],
                mapping[clause]["compliance_test_id"],
            )
            self.assertTrue(mapping[clause]["evidence"]["result_source"])
        references = solution["normative_references"]
        self.assertEqual(references["status"], "active")
        self.assertEqual(set(references["applicable_amendments"]), EXPECTED_AMENDMENTS)
        self.assertEqual(
            references["source_url"],
            "https://protect.gost.ru/sp/details/c8580ef4-7e8e-4694-808f-11f5696cb131",
        )
        self.assertEqual(
            set(references["amendment_source_urls"]),
            {
                "https://protect.gost.ru/sp/changesdetails/cd44ca83-ba0f-43e3-a8d6-ac337c961090",
                "https://protect.gost.ru/sp/changesdetails/0e7eda89-c653-47ba-8355-82867368aeeb",
                "https://protect.gost.ru/sp/changesdetails/d9f1b091-6a91-4c03-923f-d4fe0639ef71",
            },
        )
        self.assertEqual(references["checked_on"], "2026-09-03")
        self.assertTrue(references["status_evidence"])
        self.assertEqual(references["harmful_substance_standard"], "GOST 12.1.005-88")
        self.assertEqual(
            references["harmful_substance_standard_edition_input"],
            EXPECTED_GOST_EDITION,
        )
        self.assertEqual(references["status"], "active")
        self.assertEqual(references["checked_on"], "2026-09-03")
        self.assertIn("registry", references["status_evidence"].lower())

    def test_conditional_gate_fire_and_redundancy_requirements_are_evaluated(self):
        solution = load_solution()
        inputs = solution["inputs"]
        gate = solution["conditional_design_checks"]["air_thermal_curtain"]
        self.assertTrue(gate["conditional"])
        self.assertTrue(gate["applicability_inputs"])
        gate_cases = gate["illustrative_cases"]
        self.assertEqual(
            {case["input_state"] for case in gate_cases},
            {"curtain_conditions_met", "curtain_conditions_not_met"},
        )
        self.assertEqual(
            {case["decision"] for case in gate_cases},
            {"required", "not_required"},
        )
        for case in gate_cases:
            self.assertEqual(case["origin"], "illustrative_verification_input")
            self.assertTrue(case["evidence"])
        gate_project_inputs = available_project_inputs(
            inputs, AIR_CURTAIN_PROJECT_INPUTS
        )
        gate_missing_inputs = AIR_CURTAIN_PROJECT_INPUTS - set(gate_project_inputs)
        self.assertEqual(
            gate["project_applicability_inputs"], gate_project_inputs
        )
        if gate_missing_inputs:
            self.assertEqual(gate["project_decision"], "pending_missing_input")
            self.assertEqual(
                set(gate["missing_project_inputs"]), gate_missing_inputs
            )
        else:
            heated = input_value(inputs, "heated_status") == "heated"
            external_gates = input_value(inputs, "external_entry_exit_gates_present") is True
            spaces = input_value(inputs, "parking_space_count")
            expected_gate_decision = (
                "required"
                if heated and external_gates and spaces >= 50
                else "not_required"
            )
            self.assertEqual(gate["project_decision"], expected_gate_decision)
            for record in gate_project_inputs.values():
                assert_assumption_intent(self, record, "air_thermal_curtain")
            parking_record = gate_project_inputs["parking_space_count"]
            if parking_record["origin"] == "design_assumption":
                if expected_gate_decision == "required":
                    self.assertGreaterEqual(spaces, 50)
                else:
                    self.assertLess(spaces, 50)
            if contains_design_assumption(gate_project_inputs):
                self.assertIn("conditional", gate["decision_evidence"])

        dampers = solution["conditional_design_checks"]["fire_dampers"]
        self.assertTrue(dampers["applicability_inputs"])
        damper_cases = dampers["illustrative_cases"]
        self.assertEqual(
            {case["decision"] for case in damper_cases},
            {"applicable", "inapplicable"},
        )
        for case in damper_cases:
            self.assertTrue(case["evidence"])
        damper_project_inputs = available_project_inputs(
            inputs, FIRE_DAMPER_PROJECT_INPUTS
        )
        damper_missing_inputs = FIRE_DAMPER_PROJECT_INPUTS - set(
            damper_project_inputs
        )
        self.assertEqual(
            dampers["project_applicability_inputs"], damper_project_inputs
        )
        if damper_missing_inputs:
            self.assertEqual(dampers["project_decision"], "pending_missing_input")
            self.assertEqual(
                set(dampers["missing_project_inputs"]), damper_missing_inputs
            )
        else:
            expected_damper_decision = (
                "applicable"
                if input_value(inputs, "ventilation_crosses_fire_compartment_boundaries")
                else "inapplicable"
            )
            self.assertEqual(dampers["project_decision"], expected_damper_decision)
            for record in damper_project_inputs.values():
                assert_assumption_intent(self, record, "fire_damper")
            if contains_design_assumption(damper_project_inputs):
                self.assertIn("conditional", dampers["project_decision_evidence"])
        self.assertEqual(dampers["regulation_clause"], "8.3.11")

        redundancy = solution["conditional_design_checks"]["redundancy"]
        self.assertEqual(
            redundancy["condition"], "underground_parking_more_than_25_spaces"
        )
        self.assertEqual(redundancy["requirement_if_condition"], "100_percent_reserve")
        redundancy_cases = redundancy["illustrative_cases"]
        self.assertEqual(
            {case["input_state"] for case in redundancy_cases},
            {
                "underground_and_more_than_25_spaces",
                "not_underground_or_25_or_fewer_spaces",
            },
        )
        self.assertEqual(
            {case["decision"] for case in redundancy_cases},
            {"100_percent_reserve_required", "not_required"},
        )
        for case in redundancy_cases:
            self.assertEqual(case["origin"], "illustrative_verification_input")
            self.assertTrue(case["evidence"])
        redundancy_project_inputs = available_project_inputs(
            inputs, REDUNDANCY_PROJECT_INPUTS
        )
        redundancy_missing_inputs = (
            REDUNDANCY_PROJECT_INPUTS - set(redundancy_project_inputs)
        )
        self.assertEqual(
            redundancy["project_applicability_inputs"], redundancy_project_inputs
        )
        if redundancy_missing_inputs:
            self.assertEqual(
                redundancy["project_decision"], "pending_missing_input"
            )
            self.assertEqual(
                set(redundancy["missing_project_inputs"]),
                redundancy_missing_inputs,
            )
        else:
            spaces = input_value(inputs, "parking_space_count")
            expected_redundancy_decision = (
                "100_percent_reserve_required"
                if input_value(inputs, "garage_location_type") == "underground"
                and spaces > 25
                else "not_required"
            )
            self.assertEqual(
                redundancy["project_decision"], expected_redundancy_decision
            )
            for record in redundancy_project_inputs.values():
                assert_assumption_intent(self, record, "redundancy")
            parking_record = redundancy_project_inputs["parking_space_count"]
            if parking_record["origin"] == "design_assumption":
                if expected_redundancy_decision == "100_percent_reserve_required":
                    self.assertGreater(spaces, 25)
                else:
                    self.assertLessEqual(spaces, 25)
            if contains_design_assumption(redundancy_project_inputs):
                self.assertIn("conditional", redundancy["decision_evidence"])

    def test_design_report_preserves_requirement_origins_and_complete_traceability(self):
        solution = load_solution()
        report = solution["design_report"]
        self.assertEqual(report["path"], "Solutions/001-garage-ventilation/solution.md")
        self.assertTrue(report["traceability_complete"])
        self.assertTrue(report["required_sections"])
        report_path = Path(__file__).parents[3] / report["path"]
        self.assertTrue(report_path.is_file())
        report_text = report_path.read_text(encoding="utf-8").lower()
        for required_text in (
            "360 m3",
            "8.3.10",
            "co",
            "nox",
            "solvent",
            "freeze",
            "traceability",
        ):
            self.assertIn(required_text, report_text)
        traceability = solution["traceability"]
        self.assertTrue(traceability)
        origins = {item["origin"] for item in traceability}
        self.assertTrue({"regulatory", "user"}.issubset(origins))
        self.assertTrue(origins.issubset({"regulatory", "user"}))
        actual = {
            (
                item["task_object"],
                item["regulation_clause"],
                item["regulation_requirement"],
                item["acceptance_criterion"],
                item["compliance_test_id"],
                item["origin"],
            )
            for item in traceability
        }
        expected_with_origins = {
            (*row, EXPECTED_TRACEABILITY_ORIGINS[row])
            for row in EXPECTED_TRACEABILITY
        }
        self.assertEqual(actual, expected_with_origins)
        for item in traceability:
            self.assertIn(
                (
                    item["task_object"],
                    item["regulation_clause"],
                    item["regulation_requirement"],
                    item["acceptance_criterion"],
                    item["compliance_test_id"],
                    item["origin"],
                ),
                expected_with_origins,
            )


if __name__ == "__main__":
    unittest.main()
