import unittest
from model.Validator import Validator


class TestValidatorHasValidGender(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_has_valid_gender_M(self):
        raw_data = "M"
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_gender_F(self):
        raw_data = "F"
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_gender_lowercase(self):
        raw_data = "f"
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_gender_with_trailing_white_spaces(self):
        raw_data = " M "
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_gender_with_word(self):
        raw_data = "male"
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_gender_with_non_alphabetic_chars(self):
        raw_data = "m%$#"
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_gender_empty(self):
        raw_data = ""
        is_valid = self.validator.has_valid_gender(raw_data)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()
