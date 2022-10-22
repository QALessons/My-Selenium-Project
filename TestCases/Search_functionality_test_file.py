import time
import unittest
from Src.Pages.Navigation_bar_file import NavigationBarClass
from TestCases.Base_test_file import BaseTestClass


class SearchFunctionality(BaseTestClass):
    def setUp(self):
        self.mainPageObj = NavigationBarClass(self.driver)

    def test_amazon_search_functionality(self):
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon.com. Spend less. Smile more.", self.driver.title)

        self.mainPageObj.fill_in_search_field()
        self.mainPageObj.click_into_submit_button()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
