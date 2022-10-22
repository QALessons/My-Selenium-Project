from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageClass:
    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, element):
        element.click()

    def double_click(self, element):
        element.double_click()

    def click_and_hold(self):
        element = ActionChains(self.driver)
        element.click_and_hold()

    def perform(self):
        element = ActionChains(self.driver)
        element.perform()

    def set_text(self, element, text):
        element = ActionChains(self.driver)
        element.send_keys_to_element(element, text)

    def get_text(self, element):
        element.text()

    def clear_text(self, element):
        element.clear()

    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print("ERROR 3: Couldn't find the element with such locator")
            print(e)
            exit(3)

    def find_elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            print("ERROR 3: Element Not Found Exception")
            print(e)
            exit(3)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
