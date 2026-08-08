from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases.json"

EXPECTED_CATEGORIES = {
    "simple",
    "debug",
    "refactor_scope",
    "complex",
    "ambiguous",
    "destructive",
}
EXPECTED_ROUTES = {
    "EXECUTE_DIRECTLY",
    "EXPLORE_FIRST",
    "PLAN_FIRST",
    "SPEC_FIRST",
    "ASK_USER",
}
REQUIRED_FIELDS = {
    "id",
    "category",
    "input",
    "expected_route",
    "must_include",
    "must_avoid",
    "question_behavior",
    "notes",
}


class EvaluationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(CASES.read_text(encoding="utf-8"))

    def test_exactly_six_pressure_cases(self):
        self.assertEqual(6, len(self.cases))

    def test_categories_cover_agreed_risk_classes(self):
        self.assertEqual(EXPECTED_CATEGORIES, {case["category"] for case in self.cases})

    def test_cases_have_required_fields_and_valid_routes(self):
        ids = set()
        for case in self.cases:
            self.assertEqual(REQUIRED_FIELDS, set(case))
            self.assertNotIn(case["id"], ids)
            ids.add(case["id"])
            self.assertIn(case["expected_route"], EXPECTED_ROUTES)
            self.assertTrue(case["input"].strip())
            self.assertTrue(case["must_include"])
            self.assertIsInstance(case["must_avoid"], list)
            self.assertTrue(case["question_behavior"].strip())

    def test_simple_case_stays_lightweight(self):
        case = next(c for c in self.cases if c["category"] == "simple")
        self.assertEqual("EXECUTE_DIRECTLY", case["expected_route"])
        self.assertEqual("zero", case["question_behavior"])

    def test_ambiguous_destructive_case_requires_question(self):
        case = next(c for c in self.cases if c["category"] == "ambiguous")
        self.assertEqual("ASK_USER", case["expected_route"])
        self.assertIn("one_critical_question", case["question_behavior"])


if __name__ == "__main__":
    unittest.main()
