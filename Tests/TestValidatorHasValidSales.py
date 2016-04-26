import unittest
from model.Validator import Validator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_has_valid_sales_good_input(self):
        raw_data = "567"
        is_valid = self.validator.has_valid_sales(raw_data)
        self.assertTrue(is_valid)

    def test_has_valid_sales_sales_with_trailing_white_spaces(self):
        raw_data = " 787 "
        is_valid = self.validator.has_valid_sales(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_sales_with_not_numeric_chars(self):
        raw_data = "a$3"
        is_valid = self.validator.has_valid_sales(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_sales_too_short(self):
        raw_data = "26"
        is_valid = self.validator.has_valid_sales(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_sales_too_long(self):
        raw_data = "2235"
        is_valid = self.validator.has_valid_sales(raw_data)
        self.assertFalse(is_valid)

    def test_has_valid_sales_empty(self):
        raw_data = ""
        is_valid = self.validator.has_valid_sales(raw_data)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
