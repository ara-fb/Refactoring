import unittest
import unittest
import unittest.mock as mock
from model.Processor import Processor
from model.Editor import Editor
from unittest.mock import MagicMock


class TestProcessorFunctionality(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()
        self.database = self.processor.database
        bad_data = ['N52,F,57,346,Normal,98',
                    ' N520,F,57,346,Normal,98',
                    'N5#@20,F,57,346,Normal,98',
                    'N520,Female,57,346,Normal,98',
                    'N520,male,57,346,Normal,98',
                    'N520,-,57,346,Normal,98',
                    'N520,M,at,346,Normal,98',
                    'N520,M,-,346,Normal,98',
                    'N520,M,57,-,Normal,98',
                    'N520,M,57,346,-,98',
                    'N520,M,57,346,Normal,-']
        self.processor.validator.add_bad_data(bad_data)

    def test_process_bad(self):

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
