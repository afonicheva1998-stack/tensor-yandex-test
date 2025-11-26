from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[name='text']")
    SUGGEST = (By.CSS_SELECTOR, "div[data-testid='suggest']")
    IMAGES_LINK = (By.CSS_SELECTOR, "a[href*='images']")

    def enter_search(self, text):
        self.find(self.SEARCH_FIELD).send_keys(text)

    def suggest_visible(self):
        return self.is_visible(self.SUGGEST)

    def press_enter(self):
        self.find(self.SEARCH_FIELD).send_keys(Keys.ENTER)

    def go_images(self):
        self.click(self.IMAGES_LINK)
