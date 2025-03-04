from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from pages.base_paged import BrowserAutomation

class NewOrderHeader:
    def __init__(self, browser):
        self.browser = browser
        self.fake = Faker()

    def fill_order_form(self):
        self.browser.get("https://preprod.softmg.ru/")

        name = self.fake.first_name()
        email = self.fake.email()
        phone = self.fake.phone_number()
        project_description = self.fake.text()

        header_button_selector = "(//button[@class='_button_1anfh_27 _button--dot_1anfh_237 _button--sm_1anfh_40'])"
        self.browser.find_element(By.XPATH, header_button_selector).click()
        self.browser.find_element(By.XPATH, "//input[@name='name' and @placeholder='Ваше имя']").send_keys(name)
        self.browser.find_element(By.XPATH, "(//input[@name='email' and @placeholder='E-mail *'])[2]").send_keys(email)
        self.browser.find_element(By.XPATH, "(//input[@name='phone' and @placeholder='Телефон'])[2]").send_keys(phone)
        self.browser.find_element(By.XPATH, "(//textarea[@placeholder='Напишите кратко о проекте'])[2]").send_keys(project_description)

        submit_button_selector = 'button._button_1anfh_27._button--violet_1anfh_58._button--lg_1anfh_52._custom-button_1uhw6_321'
        submit_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, submit_button_selector))
        )
        submit_button.click()