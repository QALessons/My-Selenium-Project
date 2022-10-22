import time
from Src.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass
from Common.Variables.Variables_file import VariablesClass
from Src.Pages.Navigation_bar_file import NavigationBarClass
from Src.Pages.My_Card_page_file import CartPageClass


class ClearCart(BaseTestClass):
    def setUp(self):
        self.signInPageObj = SignInPageClass(self.driver)
        self.navigationBarObj = NavigationBarClass(self.driver)
        self.cardPageObj = CartPageClass(self.driver)

    def test_amazon_clear_card(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        # Sign in part
        # Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()
        # Password Part
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        time.sleep(2)  # added to not get robot check
        self.signInPageObj.click_into_sign_in_button()
        time.sleep(5)

        # Start clear Card functionality
        self.navigationBarObj.click_on_cart_button()
        self.cardPageObj.remove_all_elements_from_cart()

    def tearDown(self):
        self.driver.close()
