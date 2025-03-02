from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Настройки браузера
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

try:
    browser.get("https://preprod.softmg.ru/")

    elements = EnumerationElements(browser)

    # Клик по всем элементам из списка
    elements.click_all_elements()

    # Или выборочно
    # elements.click_elements_by_text("Ресторан", "Авто")
finally:
    browser.quit()
