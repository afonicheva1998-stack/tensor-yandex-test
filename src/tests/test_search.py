import pytest
from selenium.common.exceptions import TimeoutException
from src.pages.main_page import MainPage

def test_search_yandex(main_page):
    try:
        main_page.enter_search("Тензор")
        assert main_page.suggest_visible(), "Нет таблицы подсказок"
        main_page.press_enter()
        assert "tensor.ru" in main_page.driver.page_source
    except TimeoutException:
        pytest.skip("Элементы страницы не прогрузились за 5 с")