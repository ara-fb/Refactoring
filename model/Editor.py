from model.Validator import *
from model.Person import *


class Editor(object):

    def __init__(self):
        self._raw_data = None
        self._good_data = {}

    def set_raw(self, new_data):
        self._raw_data = new_data

    def edit_or_delete(self, a_string, action):
        if action == 'E':
            self.validate(a_string)
        elif action == 'D':
            self.remove_from_raw(a_string)

    def remove_from_raw(self, the_string):
        if the_string in self._raw_data:
            self._raw_data.remove(the_string)

    def __unpack_list(self, a_list):
        total_fields = 6
        for index in range(len(a_list), total_fields):
            a_list.append("")
        return a_list[0], a_list[1], a_list[2], a_list[3], a_list[4], a_list[5]

    def validate(self, a_string):
        list_ = Validator.clean_input(a_string)
        id_, gender, age, sales, bmi, income = self.__unpack_list(list_)

        while not Validator.has_valid_id(id_):
            id_ = Validator.clean_id(self.set_new_value(id_, "A123", "id"))

        while not Validator.has_valid_gender(gender):
            gender = Validator.clean_gender(self.set_new_value(gender, "M", "gender"))

        while not Validator.has_valid_age(age):
            age = Validator.clean_age(self.set_new_value(age, "01", "age"))

        while not Validator.has_valid_sales(sales):
            sales = Validator.clean_sales(self.set_new_value(sales, "001", "sales"))

        while not Validator.has_valid_bmi(bmi):
            bmi = Validator.clean_bmi(self.set_new_value(bmi, "Normal, Overweight, Obesity, Underweight", "bmi"))

        while not Validator.has_valid_income(income):
            income = Validator.clean_income(self.set_new_value(income, "00-100", "income"))

        p = Person(Validator.clean_id(id_), Validator.clean_gender(gender), Validator.clean_age(age), Validator.clean_sales(sales), Validator.clean_bmi(bmi), Validator.clean_income(income))

        self._good_data.update({p.get_id(): p})
        self._raw_data.remove(a_string)
        return p

    def set_new_value(self, bad_input, correct_input, value):
        prompt = "The current " + value + " is: " + bad_input + "\nThe correct format is: " + correct_input + "\nSet a new " + value + ":\n"
        return input(prompt)

    def export_good_data(self):
        return self._good_data

    def export_bad_data(self):
        return self._raw_data