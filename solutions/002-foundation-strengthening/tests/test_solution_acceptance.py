"""
SDDTDD SPEC: tasks/002-foundation-strengthening/SPEC.md

These are implementation-independent acceptance tests for the proposed
engineering solution. They evaluate the solution artifact at its public file
boundary and do not provide any production implementation.

RED stage: all tests must FAIL because the solution artifact is absent.
"""

import json
import unittest
from pathlib import Path


SOLUTION_PATH = Path(__file__).parents[1] / "solution.json"

# --- Expected normative mapping ---

EXPECTED_NORMATIVE_CLAUSES = {
    "SP45_5.3": {
        "document": "SP 45.133330",
        "clause": "5.3",
        "requirement": "foundation_base_bearing_capacity",
        "acceptance_criterion": "AC2",
    },
    "SP45_5.6": {
        "document": "SP 45.133330",
        "clause": "5.6",
        "requirement": "settlement_calculation",
        "acceptance_criterion": "AC3",
    },
    "SP45_13.3": {
        "document": "SP 45.133330",
        "clause": "13.3",
        "requirement": "strengthening_existing_foundations",
        "acceptance_criterion": "AC1",
    },
    "SP16_6.1": {
        "document": "SP 16.13330",
        "clause": "6.1",
        "requirement": "limit_state_calculation",
        "acceptance_criterion": "AC4",
    },
    "SP16_6.2": {
        "document": "SP 16.13330",
        "clause": "6.2",
        "requirement": "strength",
        "acceptance_criterion": "AC4",
    },
    "SP16_6.3": {
        "document": "SP 16.13330",
        "clause": "6.3",
        "requirement": "deformations_and_reinforcement",
        "acceptance_criterion": "AC7",
    },
    "SP16_8.3": {
        "document": "SP 16.13330",
        "clause": "8.3",
        "requirement": "strengthening_of_structures",
        "acceptance_criterion": "AC6",
    },
    "SP22_5": {
        "document": "SP 22.13330",
        "clause": "5",
        "requirement": "deformation_based_calculation",
        "acceptance_criterion": "AC3",
    },
    "GOST25100": {
        "document": "GOST 25100-2012",
        "clause": "sections 4-7",
        "requirement": "soil_classification",
        "acceptance_criterion": "AC1",
    },
    "GOST18105": {
        "document": "GOST 18105-2010",
        "clause": "all",
        "requirement": "concrete_strength_control",
        "acceptance_criterion": "AC8",
    },
    "GOST5781": {
        "document": "GOST 5781-82",
        "clause": "all",
        "requirement": "reinforcement_classes",
        "acceptance_criterion": "AC7",
    },
    "GOST10922": {
        "document": "GOST 10922-2012",
        "clause": "all",
        "requirement": "welded_joint_requirements",
        "acceptance_criterion": "AC7",
    },
    "SP35_6": {
        "document": "SP 35.13330",
        "clause": "6",
        "requirement": "earthworks",
        "acceptance_criterion": "AC9",
    },
    "SP42_6": {
        "document": "SP 42.13330",
        "clause": "6",
        "requirement": "corrosion_protection",
        "acceptance_criterion": "AC9",
    },
}

# --- Expected engineering objects ---

EXPECTED_ENGINEERING_OBJECTS = {
    "existing_foundation",
    "foundation_soil",
    "brick_masonry_walls",
    "existing_and_new_materials",
    "building_loads",
    "groundwater",
    "seismic_zoning",
    "construction_conditions",
}

# --- Expected user inputs ---

EXPECTED_USER_INPUTS = {
    "building_type": "old_brick_house",
    "strengthening_constraint": "without_full_replacement",
}


def load_solution():
    if not SOLUTION_PATH.exists():
        raise AssertionError(
            "The proposed engineering solution artifact is missing: "
            f"{SOLUTION_PATH}"
        )
    return json.loads(SOLUTION_PATH.read_text(encoding="utf-8"))


class FoundationStrengtheningAcceptanceTests(unittest.TestCase):
    """RED tests for AC1-AC12. All must fail because solution.json is absent."""

    # --- AC1: Method selection based on foundation type, soil, survey ---

    def test_AC1_method_selection_references_SP45_13_3(self):
        """AC1: Strengthening method is selected based on foundation type,
        soil characteristics, and survey results."""
        solution = load_solution()
        method = solution["strengthening_method"]
        self.assertIn("foundation_type", method)
        self.assertIn("soil_characteristics", method)
        self.assertIn("survey_results", method)
        self.assertEqual(method["normative_clause"], "SP 45.133330 cl. 13.3")

    # --- AC2: Base bearing capacity per SP 45.133330 cl. 5.3 ---

    def test_AC2_bearing_capacity_references_SP45_5_3(self):
        """AC2: Foundation base bearing capacity is calculated per clause 5.3."""
        solution = load_solution()
        calc = solution["calculations"]["base_bearing_capacity"]
        self.assertEqual(calc["method"], "SP 45.133330 cl. 5.3")
        self.assertIn("result", calc)
        self.assertIn("units", calc)
        self.assertEqual(calc["units"], "kPa")

    # --- AC3: Settlement per SP 45.133330 cl. 5.6 ---

    def test_AC3_settlement_references_SP45_5_6(self):
        """AC3: Settlement is calculated per clause 5.6 and does not
        exceed allowable values."""
        solution = load_solution()
        calc = solution["calculations"]["settlement"]
        self.assertEqual(calc["method"], "SP 45.133330 cl. 5.6")
        self.assertIn("total_settlement_mm", calc)
        self.assertIn("angular_distortion", calc)
        self.assertIn("allowable_total_mm", calc)
        self.assertIn("allowable_angular", calc)
        self.assertLessEqual(calc["total_settlement_mm"], calc["allowable_total_mm"])

    # --- AC4: Strengthened foundation bearing capacity >= load ---

    def test_AC4_strengthened_capacity_exceeds_load(self):
        """AC4: Bearing capacity of strengthened foundation >= building load."""
        solution = load_solution()
        calc = solution["calculations"]["strengthened_foundation"]
        self.assertIn("bearing_capacity_kN", calc)
        self.assertIn("applied_load_kN", calc)
        self.assertGreaterEqual(calc["bearing_capacity_kN"], calc["applied_load_kN"])

    # --- AC5: Foundation pressure <= soil resistance ---

    def test_AC5_pressure_within_soil_resistance(self):
        """AC5: Foundation base pressure does not exceed design soil resistance."""
        solution = load_solution()
        calc = solution["calculations"]["foundation_pressure"]
        self.assertIn("pressure_kPa", calc)
        self.assertIn("soil_resistance_kPa", calc)
        self.assertLessEqual(calc["pressure_kPa"], calc["soil_resistance_kPa"])

    # --- AC6: Bond between old and new concrete ---

    def test_AC6_bond_between_old_and_new_concrete(self):
        """AC6: Bond between existing and new concrete is ensured."""
        solution = load_solution()
        bond = solution["bond_assessment"]
        self.assertIn("method", bond)
        self.assertIn(bond["method"], {"interlocking", "roughness", "anchors",
                                        "combination"})
        self.assertIn("normative_clause", bond)
        self.assertEqual(bond["normative_clause"], "SP 16.13330 cl. 8.3")

    # --- AC7: Reinforcement per GOST 5781-82 and SP 16.13330 cl. 6.3 ---

    def test_AC7_reinforcement_per_GOST5781_and_SP16_6_3(self):
        """AC7: Reinforcement is designed per GOST 5781-82 and SP 16.13330."""
        solution = load_solution()
        rebar = solution["reinforcement"]
        self.assertIn("steel_class", rebar)
        self.assertIn("diameter_mm", rebar)
        self.assertIn("area_mm2", rebar)
        self.assertEqual(rebar["normative_document"], "GOST 5781-82")
        self.assertEqual(rebar["design_clause"], "SP 16.13330 cl. 6.3")

    # --- AC8: Concrete strength control per GOST 18105-2010 ---

    def test_AC8_concrete_strength_control_per_GOST18105(self):
        """AC8: Concrete strength is controlled per GOST 18105-2010."""
        solution = load_solution()
        concrete = solution["concrete_control"]
        self.assertEqual(concrete["normative_document"], "GOST 18105-2010")
        self.assertIn("strength_class", concrete)
        self.assertIn("control_method", concrete)

    # --- AC9: Work sequence and temporary bracing for safety ---

    def test_AC9_construction_safety_measures(self):
        """AC9: Work sequence and temporary bracing ensure safety."""
        solution = load_solution()
        safety = solution["construction_safety"]
        self.assertIn("work_sequence", safety)
        self.assertIsInstance(safety["work_sequence"], list)
        self.assertTrue(len(safety["work_sequence"]) > 0)
        self.assertIn("temporary_bracing", safety)
        self.assertTrue(safety["temporary_bracing"])
        self.assertEqual(safety["normative_clause"], "SP 42.13330 cl. 6")

    # --- AC10: All required checks performed ---

    def test_AC10_all_required_checks_present(self):
        """AC10: All required checks are performed."""
        solution = load_solution()
        checks = solution["performed_checks"]
        required = {
            "base_bearing_capacity",
            "foundation_bearing_capacity",
            "settlement",
            "bond",
            "reinforcement",
        }
        self.assertTrue(required.issubset(set(checks)))

    # --- AC11: Results are reproducible ---

    def test_AC11_results_reproducible(self):
        """AC11: Calculation results are reproducible with complete chain."""
        solution = load_solution()
        for calc_name, calc in solution["calculations"].items():
            self.assertIn("input_data", calc,
                          f"{calc_name} missing input_data")
            self.assertIn("method", calc,
                          f"{calc_name} missing method")
            self.assertIn("result", calc,
                          f"{calc_name} missing result")
            self.assertIn("source_clause", calc,
                          f"{calc_name} missing source_clause")

    # --- AC12: Normative references reflected with clause IDs ---

    def test_AC12_normative_references_with_clause_ids(self):
        """AC12: Every normative reference from Section 3 is reflected."""
        solution = load_solution()
        mapping = solution["normative_mapping"]
        mapping_ids = {item["id"] for item in mapping}
        for expected_id in EXPECTED_NORMATIVE_CLAUSES:
            self.assertIn(expected_id, mapping_ids,
                          f"Normative clause {expected_id} not in mapping")

    # --- Structural checks ---

    def test_solution_json_exists(self):
        """Solution artifact must exist."""
        load_solution()

    def test_solution_has_required_sections(self):
        """Solution must have all required top-level sections."""
        solution = load_solution()
        required_sections = {
            "solution_status",
            "inputs",
            "engineering_objects",
            "normative_mapping",
            "calculations",
            "strengthening_method",
            "bond_assessment",
            "reinforcement",
            "concrete_control",
            "construction_safety",
            "performed_checks",
            "traceability",
        }
        self.assertTrue(required_sections.issubset(set(solution.keys())))

    def test_user_inputs_preserved(self):
        """User inputs must be preserved and classified."""
        solution = load_solution()
        inputs = solution["inputs"]
        self.assertIn("user_provided", inputs)
        user = inputs["user_provided"]
        self.assertEqual(user["building_type"], "old_brick_house")
        self.assertEqual(user["strengthening_constraint"],
                         "without_full_replacement")

    def test_missing_inputs_reported(self):
        """Missing project inputs must be explicitly reported."""
        solution = load_solution()
        inputs = solution["inputs"]
        self.assertIn("missing_inputs", inputs)
        missing = inputs["missing_inputs"]
        required_missing = {
            "geotechnical_investigation",
            "foundation_survey",
            "building_loads",
            "groundwater_level",
            "climate_zone",
            "seismic_zone",
        }
        self.assertTrue(required_missing.issubset(set(missing)))


if __name__ == "__main__":
    unittest.main()
