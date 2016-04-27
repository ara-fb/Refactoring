from TestValidatorClean import *
from TestValidatorHasValidAge import *
from TestValidatorHasValidBmi import *
from TestValidatorHasValidGender import *
from TestValidatorHasValidId import *
from TestValidatorHasValidIncome import *
from TestValidatorHasValidSales import *

import unittest


def my_suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(TestValidatorClean))
    the_suite.addTest(unittest.makeSuite(TestValidatorHasValidAge))
    the_suite.addTest(unittest.makeSuite(TestValidatorHasValidBmi))
    the_suite.addTest(unittest.makeSuite(TestValidatorHasValidGender))
    the_suite.addTest(unittest.makeSuite(TestValidatorHasValidId))
    the_suite.addTest(unittest.makeSuite(TestValidatorHasValidIncome))
    the_suite.addTest(unittest.makeSuite(TestValidatorHasValidSales))

    return the_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = my_suite()
    runner.run(test_suite)
