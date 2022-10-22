from TestCases.Base_test_file import BaseTestClass
from Common.Variables.Variables_file import VariablesClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from Src.Pages.Navigation_bar_file import NavigationBarClass
from Src.Pages.Item_page_file import ItemPageClass


class AddToCartTestcase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.signInPageObj = SignInPageClass(self.driver)
        self.itemObj = NavigationBarClass(self.driver)
        self.itemObj1 = ItemPageClass(self.driver)
        self.itemObj2 = ItemPageClass(self.driver)

    def test_add_item_to_cart(self):
        # Sign-in part
        self.driver.get(VariablesClass.amazonSignInUrl)
        self.signInPageObj.fast_sign_in()

        # Search & add to cart part
        self.itemObj.fill_in_search_field()
        self.itemObj.select_item_from_search_results()
        self.itemObj1.change_quantity(2)
        self.itemObj1.click_on_add_to_cart_button()

    def tearDown(self):
        self.driver.close()
