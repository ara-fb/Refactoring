import unittest
from model.Validator import Validator


class TestValidatorClean(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_clean_id_with_lower_case(self):
        """
        given an ID with a lower case first character
        when clean_id() is called, expect an ID with an upper case first character
        """
        raw_data = 'j487'
        actual_washed = self.validator.clean_id(raw_data)
        expected_washed = "J487"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_id_too_long(self):
        """
        given an ID with too many characters
        when clean_id() is called, expect an ID with exactly 4 characters
        """
        raw_data = 'J487 45'
        actual_washed = self.validator.clean_id(raw_data)
        expected_washed = "J487"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_gender_lowercase(self):
        raw_data = "f"
        actual_washed = self.validator.clean_gender(raw_data)
        expected_washed = "F"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_gender_too_long(self):
        raw_data = "Male"
        actual_washed = self.validator.clean_gender(raw_data)
        expected_washed = "M"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_age_len_one(self):
        raw_data = "8"
        actual_washed = self.validator.clean_age(raw_data)
        expected_washed = "08"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_sales_len_one(self):
        raw_data = "8"
        actual_washed = self.validator.clean_sales(raw_data)
        expected_washed = "008"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_sales_len_two(self):
        raw_data = "87"
        actual_washed = self.validator.clean_sales(raw_data)
        expected_washed = "087"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_income_len_one(self):
        raw_data = "8"
        actual_washed = self.validator.clean_income(raw_data)
        expected_washed = "08"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_bmi_lowercase_overweight(self):
        raw_data = "overweight"
        actual_washed = self.validator.clean_bmi(raw_data)
        expected_washed = "Overweight"
        self.assertEquals(actual_washed, expected_washed)

    def test_clean_bmi_mixed_case_underweight(self):
        raw_data = "unDERweigHt"
        actual_washed = self.validator.clean_bmi(raw_data)
        expected_washed = "Underweight"
        self.assertEquals(actual_washed, expected_washed)



if __name__ == '__main__':
    unittest.main()
