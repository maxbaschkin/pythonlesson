from pages.base_paged import BrowserAutomation
from pages.page_list import EnumerationElements
from pages.new_order_header import NewOrderHeader
import pytest


# Проверка кнопок на станице
def test_enumeration():
    browser = BrowserAutomation(headless=True)
    browser.open_url("https://preprod.softmg.ru/")
    enumeration = EnumerationElements(browser.browser)
    enumeration.enumerate_and_check()
    browser.close_browser()


#Проверка формы хэдер
def test_new_order_header():
    browser_automation = BrowserAutomation(headless=True)
    browser_automation.open_url("https://preprod.softmg.ru/")
    order = NewOrderHeader(browser_automation.browser)
    order.fill_order_form()
    browser_automation.close_browser()