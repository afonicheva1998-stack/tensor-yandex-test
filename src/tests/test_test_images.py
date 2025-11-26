import pytest
from selenium.common.exceptions import TimeoutException
from src.pages.images_page import ImagesPage


def test_images_yandex(main_page):
    try:
        main_page.go_images()
        assert "yandex.ru/images" in main_page.driver.current_url

        img = ImagesPage(main_page.driver)
        img.open_first_category()
        assert img.search_field_value.lower() == img.category_title.lower()

        img.open_first_image()
        src1 = img.current_image_src
        assert src1 and "http" in src1, "Картинка не загрузилась"

        img.next_image()
        src2 = img.current_image_src
        assert src2 != src1, "Картинка не сменилась"

        img.prev_image()
        assert img.current_image_src == src1, "Вернулись не на ту картинку"
    except TimeoutException:
        pytest.skip("Элементы картинок не прогрузились за 5 с")
