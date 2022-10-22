from Src.Pages.Navigation_bar_file import NavigationBarClass
from Src.Pages.Base_page_file import BasePageClass
from selenium.webdriver.common.by import By


class CartPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocatorsClass()
        self.navigationBarObj = NavigationBarClass(driver)

    def remove_first_element_from_cart(self):
        deleteButtonElement = self.find_element(self.locators.firstProductDeleteButtonLocator)
        self.click_to_element(deleteButtonElement)

    def remove_all_elements_from_cart(self):
        while self.navigationBarObj.get_cart_products_quantity() > 0:
            self.remove_first_element_from_cart()


class CartPageLocatorsClass:
    firstProductDeleteButtonLocator = (By.XPATH, "//input[@value='Delete']")
