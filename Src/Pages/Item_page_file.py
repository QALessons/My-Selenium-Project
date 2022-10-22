from Src.Pages.Base_page_file import BasePageClass
from selenium.webdriver.common.by import By


class ItemPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemPageClassLocators()

    def click_on_add_to_cart_button(self):
        addToCartButtonElement = self.find_element(self.locators.addToCartButtonLocator)
        addToCartButtonElement.click()

    def click_on_buy_now_button(self):
        buyNowButtonElement = self.find_element(self.locators.buyNowButtonLocator)
        buyNowButtonElement.click()

    def change_quantity(self, quantity):
        try:
            itemQuantityDropdownElement = self.find_element(self.locators.itemQuantityDropdownLocator)
            itemQuantityDropdownElement.click()
            itemQuantityElement = self.find_element((By.ID, f"quantity_{quantity-1}"))
            itemQuantityElement.click()

        except Exception as NoQntty:
            print("ERROR 4: This Product isn't introduced in such quantity.")
            print(NoQntty)
            exit(4)

    def close_add_to_cart_modal(self):
        closeButtonElement = self.find_element(self.locators.closeButtonElementLocator)
        closeButtonElement.click()


class ItemPageClassLocators:
    addToCartButtonLocator = (By.ID, "add-to-cart-button")
    buyNowButtonLocator = (By.ID, "buy-now-button")
    itemQuantityDropdownLocator = (By.ID, "a-autoid-0-announce")
    closeButtonElementLocator = (By.ID, "attach-close_sideSheet-link")
