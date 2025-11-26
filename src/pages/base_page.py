from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_safe(self, locator, retries=2):
        for _ in range(retries):
            try:
                self.click(locator)
                return
            except Exception:
                pass
        raise TimeoutException("Не удалось кликнуть за 2 попытки")
