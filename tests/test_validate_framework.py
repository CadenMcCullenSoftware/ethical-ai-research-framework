import contextlib
import io
import unittest
from unittest import mock

from scripts import validate_framework


SOURCE = "First requirement.\nSecond requirement.\n"
EXPANDED = (
    "**Original point:** First requirement.\n"
    "**Illustrative example:** Example one.\n"
    "**Original point:** Second requirement.\n"
    "**Illustrative example:** Example two.\n"
)


class ValidateTextsTests(unittest.TestCase):
    def test_accepts_matching_points_and_one_example_per_point(self):
        self.assertEqual(validate_framework.validate_texts(SOURCE, EXPANDED, expected_source_count=2), [])

    def test_reports_unexpected_source_count(self):
        problems = validate_framework.validate_texts(SOURCE, EXPANDED)
        self.assertIn("Expected 44 source lines, found 2", problems)

    def test_reports_missing_preserved_point(self):
        expanded = "**Original point:** First requirement.\n**Illustrative example:** Example.\n"
        problems = validate_framework.validate_texts(SOURCE, expanded, expected_source_count=2)
        self.assertIn("Expected 2 preserved points, found 1", problems)
        self.assertIn("Source and expanded point counts differ", problems)

    def test_reports_changed_source_wording(self):
        expanded = EXPANDED.replace("First requirement.", "Altered requirement.", 1)
        problems = validate_framework.validate_texts(SOURCE, expanded, expected_source_count=2)
        self.assertTrue(any(problem.startswith("Point 1 differs from source:") for problem in problems))

    def test_reports_missing_example(self):
        expanded = EXPANDED.replace("**Illustrative example:** Example two.\n", "")
        problems = validate_framework.validate_texts(SOURCE, expanded, expected_source_count=2)
        self.assertIn("Expected one example per source point (2), found 1", problems)


class MainTests(unittest.TestCase):
    def test_main_passes_for_repository_documents(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            result = validate_framework.main()
        self.assertEqual(result, 0)
        self.assertIn("44 verbatim points and 44 examples", output.getvalue())

    def test_main_returns_failure_and_lists_problems(self):
        with (
            mock.patch.object(validate_framework, "SOURCE") as source_path,
            mock.patch.object(validate_framework, "EXPANDED") as expanded_path,
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            source_path.read_text.return_value = SOURCE
            expanded_path.read_text.return_value = ""
            result = validate_framework.main()
        self.assertEqual(result, 1)
        self.assertIn("Framework validation FAILED:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
