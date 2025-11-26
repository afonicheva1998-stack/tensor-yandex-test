import pytest
from src.utils.driver import get_driver
from src.pages.main_page import MainPage


@pytest.fixture(scope="session")
def driver():
    drv = get_driver()
    yield drv
    drv.quit()


@pytest.fixture
def main_page(driver):
    driver.get("https://yandex.ru")
    return MainPage(driver)
