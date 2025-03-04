from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserAutomation:
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()

    def open_url(self, url):
        self.browser.get(url)

    def close_browser(self):
        self.browser.quit()