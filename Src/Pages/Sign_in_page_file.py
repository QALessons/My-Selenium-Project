import time
from selenium.webdriver.common.by import By
from Common.Variables.Variables_file import VariablesClass
from Src.Pages.Base_page_file import BasePageClass


class SignInPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignInPageLocatorsClass()

    def fill_username_field(self, user_name=VariablesClass.get_username()):
        userNameTextBoxElement = self.find_element(self.locators.userNameTextFieldLocator)
        userNameTextBoxElement.send_keys(user_name)

    def click_into_continue_button(self):
        continueButtonElement = self.find_element(self.locators.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password=VariablesClass.get_password()):
        passwordTextBoxElement = self.find_element(self.locators.passwordTextFieldLocator)
        passwordTextBoxElement.send_keys(password)

    def click_into_sign_in_button(self):
        signInButtonElement = self.find_element(self.locators.signInButtonLocator)
        signInButtonElement.click()

    def check_to_keep_me_signed_in_checkbox(self):
        keepMeSignedInElement = self.find_element(self.locators.keepMeSignedInLocator)
        keepMeSignedInElement.click()

    def fast_sign_in(self, username=VariablesClass.get_username(), password=VariablesClass.get_password()):
        """
        Opens Amazon.com sign in page and singes in.
        We can specify a username and password, otherwise the default values will be used.
        """
        self.driver.get(VariablesClass.amazonSignInUrl)
        # username
        self.fill_username_field(username)
        time.sleep(2)  # added to not get robot check
        self.click_into_continue_button()
        # password
        self.fill_password_field(password)
        time.sleep(2)  # added to not get robot check
        self.click_into_sign_in_button()


class SignInPageLocatorsClass:
    # Username Part
    userNameTextFieldLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")

    # Password Part
    passwordTextFieldLocator = (By.ID, "ap_password")
    signInButtonLocator = (By.ID, "signInSubmit")
    keepMeSignedInLocator = (By.NAME, "rememberMe")
