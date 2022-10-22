import unittest
from unittest import TestLoader, TextTestRunner, TestSuite
# import HtmlTestRunner (chem karoghanum install anel package)
from TestCases.Clear_item_from_card_test_file import ClearCart
from TestCases.Search_functionality_test_file import SearchFunctionality
from TestCases.Sign_in_test_file import SignIn
from TestCases.Name_edit_test_file import EditCustomersNameTestCase
from TestCases.Add_item_to_card_test_file import AddToCartTestcase


class RunnerClass:
    pass


if __name__ == "__main__":
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TestCases/Run/Reports'))
    loader = TestLoader()

    suite = TestSuite((
        loader.loadTestsFromTestCase(SignIn),
        loader.loadTestsFromTestCase(SearchFunctionality),
        loader.loadTestsFromTestCase(AddToCartTestcase),
        loader.loadTestsFromTestCase(ClearCart),
        loader.loadTestsFromTestCase(EditCustomersNameTestCase),
    ))
    # run test
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
