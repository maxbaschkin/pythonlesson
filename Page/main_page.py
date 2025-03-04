from selenium.webdriver.common.by import By
from Page.base_base import BaseBase


button_selector = (By.XPATH, "(//button[@class='_button_1anfh_27 _button--dot_1anfh_237 _button--sm_1anfh_40'])")
result_selector = (By.XPATH, "//span[contains(@class, '_submit__form-title_')]")

class MainPage(BaseBase):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://preprod.softmg.ru/')

    def button_click(self):
        return self.find(button_selector).click()

    def result_button(self):
        return self.find(result_selector)

    def text_is_displayed(self):
        return self.text().is_displayed()
