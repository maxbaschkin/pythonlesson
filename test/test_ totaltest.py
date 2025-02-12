import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import HomePage


# Тест_№1 - Проверка кнопки "Оставить заявку" и формы (header).
def test_button_header(browser):
    home_page = HomePage(browser)
    home_page.open()
    header_button_selector = "(//button[@class='_button_1anfh_27 _button--dot_1anfh_237 _button--sm_1anfh_40'])[1]"
    browser.find_element(By.XPATH, header_button_selector).click()
    browser.find_element(By.XPATH, "(//input[@name='name' and @type='text'])[2]").send_keys("Максим")
    browser.find_element(By.XPATH, "(//input[@name='email' and @type='email'])[2]").send_keys("test@test.ru")
    browser.find_element(By.XPATH, "(//input[@name='phone' and @type='text'])[2]").send_keys("79999096909")
    browser.find_element(By.XPATH, "(//textarea[@placeholder='Напишите кратко о проекте'])[2]").send_keys(
        "Привет это тест номер 1!")
    submit_button_selector = 'button._button_1anfh_27._button--violet_1anfh_58._button--lg_1anfh_52._custom-button_1uhw6_321'
    submit_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, submit_button_selector))
    )
    submit_button.click()


# Тест_№2 - Проверка кнопки "Оставить заявку" и формы (footer).
def test_button_footer(browser):
    home_page = HomePage(browser)
    home_page.open()
    footer_button_selector = "(//button[@class='_button_1anfh_27 _button--lightWhite_1anfh_106 _button--md_1anfh_46 _button-custom_17yka_470'])"
    browser.find_element(By.XPATH, footer_button_selector).click()
    browser.find_element(By.XPATH, "(//input[@name='name' and @type='text'])[2]").send_keys("Максим")
    browser.find_element(By.XPATH, "(//input[@name='email' and @type='email'])[2]").send_keys("test@test.ru")
    browser.find_element(By.XPATH, "(//input[@name='phone' and @type='text'])[2]").send_keys("79999096909")
    browser.find_element(By.XPATH, "(//textarea[@placeholder='Напишите кратко о проекте'])[2]").send_keys(
        "Привет это тест номер 2!")
    submit_button_selector = 'button._button_1anfh_27._button--violet_1anfh_58._button--lg_1anfh_52._custom-button_1uhw6_321'
    submit_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, submit_button_selector))
    )
    submit_button.click()


# Тест_№3 - Проверка placeholder'ов footer
def test_placeholders_footer(browser):
    home_page = HomePage(browser)
    home_page.open()
    browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите кратко о проекте']").send_keys(
        'Привет это тест!')
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Как вас зовут?']").send_keys('Максим')
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='E-mail *']").send_keys('test1@test.ru')
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Телефон']").send_keys('79999096909')
    for i in range(1, 7):
        xpath = f"//div[@class='_tagsWrapper_1r0gr_27']/child::button[{i}]"
        browser.find_element(By.XPATH, xpath).click()

    browser.find_element(By.CLASS_NAME, "_buttonCustom_8kcfs_28").click()
    text_assert = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "span._typography_1f6lr_28._typography--h5_1f6lr_134._typography--black_1f6lr_319._typography--inherit_1f6lr_331"))
    )
    assert text_assert.text == "Заявка оформлена!"


# Тест_№4 - Проверка формы "Напишите нам, мы онлайн!"
def test_button_chat(browser):
    home_page = HomePage(browser)
    home_page.open()
    chat_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ws-btn-title"))
    )
    chat_button.click()
    message_input = WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='ws-textarea']"))
    )
    message_input.send_keys('Привет это тест номер 4')
    browser.find_element(By.XPATH, "//div[@class='ws-textarea-send-btn' and @title='Отправить']/child::i").click()
    name_input = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @placeholder='Иван Иванов']"))
    )
    name_input.send_keys('Максим Максимов')
    dropdown = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='ws-dcpi_dropdown-toggle']"))
    )
    dropdown.click()
    flag_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='ws-dcpi_flag ws-dcpi_flag-ru'][1]"))
    )
    flag_button.click()
    browser.find_element(By.XPATH, "//input[@type='tel' and @placeholder='Введите номер телефона']").send_keys(
        '9999096909')
    browser.find_element(By.XPATH, "//input[@type='email' and @placeholder='ivan@gmail.com'][1]").send_keys(
        'test@test.ru')
    browser.find_element(By.XPATH, "//a[text()='Готово' and @class='ws-preform-btn ws-preform-btn-save'][1]").click()


# Тест_№5 - Проверка переходов по вкладкам header'а
def test_transition(browser):
    home_page = HomePage(browser)
    home_page.open()
    for i in range(1, 6):
        item = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[@class='_firstLevelItem_x9t0k_43'][{i}]"))
        )
        item.click()
    browser.find_element(By.CSS_SELECTOR, "svg._logoSMG_kdgsi_137").click()


# Тест_№6 - Проверка переходов с главной страницы.
# Переход с раздела "Создадим сайт любой тематики"

def test_transition_createsite(browser, hrefs_test_6_1, click_button_and_logo, logo_selector):
    home_page = HomePage(browser)
    home_page.open()

    for href in hrefs_test_6_1:
        button_xpath = f"//a[@class='_button_1anfh_27 _button--gray_1anfh_149 _button--md_1anfh_46 undefined _topicStyled_zfujw_28' and @href='{href}']"
        click_button_and_logo(browser, button_xpath, logo_selector)


# Переход с раздела "Примеры работ"

def test_transition_exampleswork(browser, hrefs_test_6_2, click_button_and_logo, logo_selector):
    home_page = HomePage(browser)
    home_page.open()

    for href in hrefs_test_6_2:
        button_xpath = f"//a[@class='_item_t5d52_109' and @href='{href}']"
        click_button_and_logo(browser, button_xpath, logo_selector)


# Переход с раздела "Развивайтесь вместе с нами!"

def test_transition_devtogether(browser, hrefs_test_6_3, click_button_and_logo, logo_selector):
    home_page = HomePage(browser)
    home_page.open()

    for href in hrefs_test_6_3:
        button_xpath = f"//a[@class='_card_5arw4_49' and @href='{href}']"
        click_button_and_logo(browser, button_xpath, logo_selector)


# Переход с раздела "Создание сайта под ключ"

def test_transition_turnkey(browser, hrefs_test_7, click_button_and_logo, logo_selector):
    home_page = HomePage(browser)
    home_page.open()

    for href in hrefs_test_7:
        button_xpath = f"//a[@class='_tag_zhzvv_379' and @href='{href}']"
        click_button_and_logo(browser, button_xpath, logo_selector)
