import names
from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass
from Common.Variables.Variables_file import VariablesClass
from selenium.webdriver.common.keys import Keys


class NavigationBarClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavigationBarLocatorsClass()

    def fill_in_search_field(self, text=VariablesClass.searchText):
        searchField = self.find_element(self.locators.searchFieldLocator)
        searchField.clear()
        searchField.send_keys(text)
        searchField.send_keys(Keys.ENTER)

    def select_item_from_search_results(self, n: int = 1):
        foundElements = self.find_elements(self.locators.foundItemsLocator)
        foundItemElement = foundElements[n // 2 + n]
        foundItemElement.click()

    def click_into_submit_button(self):
        submitButton = self.find_element(self.locators.submitButton)
        submitButton.click()

    def click_on_cart_button(self):
        cartButtonElement = self.find_element(self.locators.cartButtonLocator)
        cartButtonElement.click()

    def get_cart_products_quantity(self):
        cartButtonElement = self.find_element(self.locators.cartButtonLocator)
        return int(cartButtonElement.text)

    def edit_customers_name(self):
        accountsAndListsElement = self.find_element(self.locators.accountsAndListsLocator)
        accountsAndListsElement.click()
        loginAndSecurityElement = self.find_element(self.locators.loginAndSecurityLocator)
        loginAndSecurityElement.click()
        editNameButtonElement = self.find_element(self.locators.editNameButtonLocator)
        editNameButtonElement.click()
        newNameTextBoxElement = self.find_element(self.locators.newNameTextBoxLocator)
        newNameTextBoxElement.clear()
        newNameTextBoxElement.send_keys(names.get_full_name(gender='female'))
        saveChangesButtonElement = self.find_element(self.locators.saveChangesButtonLocator)
        saveChangesButtonElement.click()


class NavigationBarLocatorsClass:
    searchFieldLocator = (By.ID, "twotabsearchtextbox")
    submitButton = (By.ID, "nav-search-submit-button")
    cartButtonLocator = (By.ID, "nav-cart-count")
    accountsAndListsLocator = (By.ID, "nav-link-accountList")
    loginAndSecurityLocator = (By.XPATH, "(//h2[@class='a-spacing-none ya-card__heading--rich a-text-normal'])[2]")
    editNameButtonLocator = (By.ID, "auth-cnep-edit-name-button")
    newNameTextBoxLocator = (By.ID, "ap_customer_name")
    saveChangesButtonLocator = (By.ID, "cnep_1C_submit_button")
    foundItemsLocator = (By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
