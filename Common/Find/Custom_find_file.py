from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomFindClass:
    def __init__(self, driver):
        self.driver = driver

    def custom_find_element(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print("ERROR 3: Element Not Found Exception")
            print(e)
            exit(3)

    def custom_find_elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            print("ERROR 3: Element Not Found Exception")
            print(e)
            exit(3)
