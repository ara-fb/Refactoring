import unittest
import unittest.mock as mock
from model.Processor import Processor
from model.Editor import Editor
from unittest.mock import MagicMock


class TestEditFunctionality(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()
        editor = Editor()
        editor.edit = MagicMock()
        self.mock_edit = editor.edit
        editor.edit_or_delete = MagicMock()
        self.edit_or_delete = editor.edit_or_delete
        editor.set_new_value = MagicMock()
        self.mock


    def test_edit(self):
        self.processor.editor.set_raw(["T109,m,74,861,-,22"])
        self.assertEqual(True, False)

    def test_editor_edit_or_delete(self):
        pass

    def test_set_validate(self):
        input_str = "T109,m,74,861,-,22"
        with mock.patch('simulating_input_demo.input') as mp:
            mp.return_value = '34'
            self.processor.editor.validate(input_str)
            self.assertNotEqual()


if __name__ == '__main__':
    unittest.main()
