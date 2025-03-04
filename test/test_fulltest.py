import pytest
from pages.base_paged import BasePage
from pages.asserts import Asserts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Данные для форм
form_data_1 = {'name': 'Максим', 'email': 'test@test.ru', 'phone': '79999096909', 'message': 'Привет это тест номер 1!'}
form_data_2 = {'name': 'Максим', 'email': 'test@test.ru', 'phone': '79999096909', 'message': 'Привет это тест номер 2!'}

# Тест_№1 - Проверка кнопки "Оставить заявку" и формы (header).
def test_button_header(browser):
    home_page = BasePage(browser)
    home_page.open()
    home_page.browser.find_element(By.XPATH, BasePage.HEADER_BUTTON_SELECTOR).click()
    home_page.fill_form(form_data_1)
    home_page.click_submit()

    assertions = Asserts(browser)
    assertions.assert_success_message("Заявка оформлена!")


# Тест_№2 - Проверка кнопки "Оставить заявку" и формы (footer).
def test_button_footer(browser):
    home_page = BasePage(browser)
    home_page.open()
    home_page.browser.find_element(By.XPATH, BasePage.FOOTER_BUTTON_SELECTOR).click()
    home_page.fill_form(form_data_2)
    home_page.click_submit()

    assertions = Asserts(browser)
    assertions.assert_success_message("Заявка оформлена!")


# Тест_№3 - Проверка placeholder'ов footer
def test_placeholders_footer(browser):
    home_page = BasePage(browser)
    home_page.open()
    home_page.fill_form(form_data_1)
    home_page.browser.find_element(By.CSS_SELECTOR, ".ws-preform-btn.ws-preform-btn-save").click()

    assertions = Asserts(browser)
    assertions.assert_success_message("Заявка оформлена!")

# Тест_№4 - Проверка формы "Напишите нам, мы онлайн!"
def test_button_chat(browser):
    home_page = BasePage(browser)
    home_page.open()
    home_page.click_chat()
    home_page.send_message("Привет это тест номер 4")
    home_page.fill_chat_form('Максим Максимов', '9999096909', 'test@test.ru')

    assertions = Asserts(browser)
    assertions.assert_message_sent("//div[contains(@class, 'sent-message-class')]")


# Тест_№5 - Проверка переходов по вкладкам header'а
def test_transition(browser):
    home_page = BasePage(browser)
    home_page.open()
    assertions = Asserts(browser)
    for i in range(1, 6):
        item = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[@class='_firstLevelItem_x9t0k_43'][{i}]"))
        )
        item.click()
    home_page.browser.find_element(By.CSS_SELECTOR, "svg._logoSMG_kdgsi_137").click()
    assertions.assert_logo_visible("svg._logoSMG_kdgsi_137")