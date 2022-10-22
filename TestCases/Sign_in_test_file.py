import time

from Src.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass
from Common.Variables.Variables_file import VariablesClass


class SignIn(BaseTestClass):
    def setUp(self):
        self.signInPageObj = SignInPageClass(self.driver)

    def test_amazon_sign_in(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        # Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()

        # Password Part
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        time.sleep(2)  # added to not get robot check
        self.signInPageObj.click_into_sign_in_button()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()

