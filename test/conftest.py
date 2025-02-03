from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()