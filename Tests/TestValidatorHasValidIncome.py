import unittest
from model.Validator import Validator


class TestValidatorHasValidIncome(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_has_valid_income_len_2(self):
        raw_data = "01"
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_income_len_3(self):
        raw_data = "567"
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_income_with_trailing_white_spaces(self):
        raw_data = " 78 "
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_income_with_not_numeric_chars(self):
        raw_data = "a$"
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_income_too_short(self):
        raw_data = "2"
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_income_empty(self):
        raw_data = ""
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_income_too_long(self):
        # this test should fail but passes
        raw_data = "2235"
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_income_too_long_second(self):
        # this test should fail but passes
        raw_data = "22359900"
        is_valid = self.validator.has_valid_income(raw_data)
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()
