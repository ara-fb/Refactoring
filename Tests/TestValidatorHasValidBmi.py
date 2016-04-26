import unittest
from model.Validator import Validator


class TestValidatorHasValidBmi(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_has_valid_bmi_Overweight(self):
        raw_data = "Overweight"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_bmi_Normal(self):
        raw_data = "Normal"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_bmi_Obesity(self):
        raw_data = "Obesity"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_bmi_Underweight(self):
        raw_data = "Underweight"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_bmi_lowercase_overweight(self):
        raw_data = "overweight"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_bmi_mixed_case_underweight(self):
        raw_data = "unDERweigHt"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_bmi_with_trailing_white_spaces(self):
        raw_data = " normal "
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_bmi_with_non_alphabetic_chars(self):
        raw_data = "0besit%"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_bmi_misspelled(self):
        raw_data = "Overwieght"
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_bmi_empty(self):
        raw_data = ""
        is_valid = self.validator.has_valid_bmi(raw_data)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
