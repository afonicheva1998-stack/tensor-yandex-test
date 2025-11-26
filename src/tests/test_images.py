import pytest
from selenium.common.exceptions import TimeoutException
from src.pages.images_page import ImagesPage


def test_images_yandex(main_page):
    main_page.go_images()
    assert "yandex.ru/images" in main_page.driver.current_url
    img = ImagesPage(main_page.driver)
    img.open_first_category()
    assert img.search_field_value == img.category_title
    img.open_first_image()
    src1 = img.current_image_src
    img.next_image()
    src2 = img.current_image_src
    assert src1 != src2, "Картинка не сменилась"
    img.prev_image()
    assert img.current_image_src == src1, "Вернулись не на ту картинку"
