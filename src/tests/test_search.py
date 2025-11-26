from src.pages.main_page import MainPage
from selenium.webdriver.common.keys import Keys

def test_search_yandex(main_page):
    main_page.enter_search("Тензор")
    assert main_page.suggest_visible(), "Нет таблицы подсказок"
    main_page.press_enter()
    assert "tensor.ru" in main_page.driver.page_source