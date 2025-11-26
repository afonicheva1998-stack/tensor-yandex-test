from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ImagesPage(BasePage):
    FIRST_CATEGORY = (By.CSS_SELECTOR, "div.cl-teaser__wrap")
    SEARCH_FIELD   = (By.CSS_SELECTOR, "input[name='text']")
    FIRST_IMAGE    = (By.CSS_SELECTOR, "img.cl-teaser__image")
    IMG_VIEWER     = (By.CSS_SELECTOR, "img[class*='image__image']")
    NEXT_BTN       = (By.CSS_SELECTOR, "button[class*='__button_type_next']")
    PREV_BTN       = (By.CSS_SELECTOR, "button[class*='__button_type_prev']")

    def open_first_category(self):
        self.click(self.FIRST_CATEGORY)

    @property
    def category_title(self):
        return self.find(self.FIRST_CATEGORY).text

    @property
    def search_field_value(self):
        return self.find(self.SEARCH_FIELD).get_attribute("value")

    def open_first_image(self):
        self.click(self.FIRST_IMAGE)

    @property
    def current_image_src(self):
        return self.find(self.IMG_VIEWER).get_attribute("src")

    def next_image(self):
        self.click(self.NEXT_BTN)

    def prev_image(self):
        self.click(self.PREV_BTN)