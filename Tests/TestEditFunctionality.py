import unittest
import unittest.mock as mock
from model.Processor import Processor
from model.Editor import Editor
from unittest.mock import MagicMock
from model.Person import Person


class TestEditFunctionality(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()
        # editor = Editor()
        # editor.edit = MagicMock()
        #self.mock_edit = editor.edit
        # editor.edit_or_delete = MagicMock()
        # self.edit_or_delete = editor.edit_or_delete
        # editor.set_new_value = MagicMock()

    def test_editor_edit_or_delete(self):
        pass

    def test_set_validate_valid_all(self):
        input_str = "T109,m,74,861,Normal,22"
        self.processor.editor.set_raw(["T109,m,74,861,Normal,22"])
        e_id,e_gender, e_age, e_sales,e_bmi, e_income = 'T109','M','74','861','Normal','22'
        actual_person = self.processor.editor.validate(input_str)
        self.assertEquals(actual_person.get_id(),e_id)
        self.assertEquals(actual_person.get_gender(),e_gender)
        self.assertEquals(actual_person.get_age(),e_age)
        self.assertEquals(actual_person.get_sales(),e_sales)
        self.assertEquals(actual_person.get_bmi(),e_bmi)
        self.assertEquals(actual_person.get_income(),e_income)


    def test_set_validate_too_short(self):
        with mock.patch('builtins.input', return_value='22'):
            input_str = "T109,m,74,861,Normal"
            self.processor.editor.set_raw(["T109,m,74,861,Normal"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income = 'T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)


    def test_set_validate_invalid_id(self):
        with mock.patch('builtins.input', return_value='T109'):
            input_str = "=,m,74,861,Normal,22"
            self.processor.editor.set_raw(["=,m,74,861,Normal,22"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income  = 'T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)

    def test_set_validate_invalid_gender(self):
        with mock.patch('builtins.input', return_value='M'):
            input_str = "T109,-,74,861,Normal,22"
            self.processor.editor.set_raw(["T109,-,74,861,Normal,22"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income  = 'T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)

    def test_set_validate_invalid_age(self):
        with mock.patch('builtins.input', return_value='74'):
            input_str = "T109,m,-,861,Normal,22"
            self.processor.editor.set_raw(["T109,m,-,861,Normal,22"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income = 'T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)

    def test_set_validate_invalid_sales(self):
        with mock.patch('builtins.input', return_value='861'):
            input_str = "T109,m,74,-,Normal,22"
            self.processor.editor.set_raw(["T109,m,74,-,Normal,22"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income ='T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)

    def test_set_validate_invalid_bmi(self):
        with mock.patch('builtins.input', return_value='Normal'):
            input_str = "T109,m,74,861,-,22"
            self.processor.editor.set_raw(["T109,m,74,861,-,22"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income = 'T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)

    def test_set_validate_invalid_income(self):
        with mock.patch('builtins.input', return_value='22'):
            input_str = "T109,m,74,861,Normal,-"
            self.processor.editor.set_raw(["T109,m,74,861,Normal,-"])
            e_id,e_gender, e_age, e_sales,e_bmi, e_income = 'T109','M','74','861','Normal','22'
            actual_person = self.processor.editor.validate(input_str)
            self.assertEquals(actual_person.get_id(),e_id)
            self.assertEquals(actual_person.get_gender(),e_gender)
            self.assertEquals(actual_person.get_age(),e_age)
            self.assertEquals(actual_person.get_sales(),e_sales)
            self.assertEquals(actual_person.get_bmi(),e_bmi)
            self.assertEquals(actual_person.get_income(),e_income)

if __name__ == '__main__':
    unittest.main()
