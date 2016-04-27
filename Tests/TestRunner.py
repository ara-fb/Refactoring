from Tests.TestValidatorClean import *
from Tests.TestValidatorHasValidAge import *
from Tests.TestValidatorHasValidBmi import *
from Tests.TestValidatorHasValidGender import *
from Tests.TestValidatorHasValidId import *
from Tests.TestValidatorHasValidIncome import *
from Tests.TestValidatorHasValidSales import *
from Tests.TestEditFunctionality import *

import unittest


def my_suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(TestEditFunctionality))
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
