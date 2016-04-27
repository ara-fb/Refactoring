import unittest
from model.Validator import Validator


class TestValidatorHasValidAge(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_has_valid_age_good_age(self):
        raw_age_data = "01"
        is_valid = self.validator.has_valid_age(raw_age_data)
        self.assertTrue(is_valid)

    def test_has_valid_age_with_trailing_white_spaces(self):
        raw_age_data = " 78 "
        is_valid = self.validator.has_valid_age(raw_age_data)
        self.assertFalse(is_valid)

    def test_has_valid_age_with_not_numeric_chars(self):
        raw_age_data = "ab"
        is_valid = self.validator.has_valid_age(raw_age_data)
        self.assertFalse(is_valid)

    def test_has_valid_age_too_short(self):
        raw_age_data = "2"
        is_valid = self.validator.has_valid_age(raw_age_data)
        self.assertFalse(is_valid)

    def test_has_valid_age_too_long(self):
        raw_age_data = "223"
        is_valid = self.validator.has_valid_age(raw_age_data)
        self.assertFalse(is_valid)

    def test_has_valid_age_empty(self):
        raw_age_data = ""
        is_valid = self.validator.has_valid_age(raw_age_data)
        self.assertFalse(is_valid)



if __name__ == '__main__':
    unittest.main()
