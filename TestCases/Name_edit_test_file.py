import time
from TestCases.Base_test_file import BaseTestClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from Common.Variables.Variables_file import VariablesClass
from Src.Pages.Navigation_bar_file import NavigationBarClass


class EditCustomersNameTestCase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.signInPageObj = SignInPageClass(self.driver)
        self.navigationBarObj = NavigationBarClass(self.driver)

    def test_username_edit(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        # Sign-in part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()
        self.signInPageObj.fill_password_field()
        self.signInPageObj.click_into_sign_in_button()

        # Name edit part
        self.navigationBarObj.edit_customers_name()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
