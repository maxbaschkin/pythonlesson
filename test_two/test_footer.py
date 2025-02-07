import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_footer():
    browser = webdriver.Chrome()
    browser.get("https://preprod.softmg.ru/")
    browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите кратко о проекте']").send_keys('Привет это тест!')
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Как вас зовут?']").send_keys('Максим')
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='E-mail *']").send_keys('test1@test.ru')
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Телефон']").send_keys('79999096909')
    browser.find_element(By.CLASS_NAME, "_buttonCustom_8kcfs_28").click()
    text_assert = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "span._typography_1f6lr_28._typography--h5_1f6lr_134._typography--black_1f6lr_319._typography--inherit_1f6lr_331"))
    )
    assert text_assert.text == "Заявка оформлена!"

