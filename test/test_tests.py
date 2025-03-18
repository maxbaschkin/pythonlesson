import pytest
from pages.new_order_header import NewOrderHeader
from pages.new_order_footer import NewOrderFooter
from pages.placeholder_footer import PlaceholderFooter


# Тест №1 Открытие и заполнение формы "Оставить заявку" (Header)
def test_new_order_header(browser):
    header = NewOrderHeader(headless=True)
    header.browser = browser
    header.open_url("https://preprod.softmg.ru")
    header.click_header_button()
    header.fill_form()
    header.submit_form()
    header.validate_submission()


# Тест №2 Открытие и заполнение формы "Оставить заявку" (Footer)
def test_new_order_footer(browser):
    footer = NewOrderFooter(headless=True)
    footer.browser = browser
    footer.open_url("https://preprod.softmg.ru/")
    footer.click_footer_button()
    footer.fill_form()
    footer.submit_form()
    footer.validate_submission()


# Тест №3 Проверка формы "Обсудить проект" (Footer)
def test_placeholders_footer(browser):
    placeholder_form = PlaceholderFooter(headless=True)
    placeholder_form.browser = browser
    placeholder_form.open_url("https://preprod.softmg.ru/")
