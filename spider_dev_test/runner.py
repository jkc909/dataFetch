import unittest

import test_all_data
import test_summoner
import test_amazon



loader = unittest.TestLoader()
suite = unittest.TestSuite()

# suite.addTests(loader.loadTestsFromModule(test_all_data))
# suite.addTests(loader.loadTestsFromModule(test_summoner))
suite.addTests(loader.loadTestsFromModule(test_amazon))
# print(suite)

runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)

