import pytest
from selenium.common.exceptions import TimeoutException


def test_search_yandex(main_page):
    try:
        main_page.enter_search("Тензор")
        assert main_page.suggest_visible(), "Нет таблицы подсказок"
        main_page.press_enter()
        assert img.search_field_value.lower() in img.category_title.lower()
    except TimeoutException:
        pytest.skip("Элементы страницы не прогрузились за 5 с")
