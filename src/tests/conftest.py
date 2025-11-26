import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from src.utils.driver import get_driver
from src.pages.main_page import MainPage


@pytest.fixture(scope="session")
def driver():
    drv = get_driver()
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


@pytest.fixture
def main_page(driver):
    driver.get("https://yandex.ru")
    return MainPage(driver)
