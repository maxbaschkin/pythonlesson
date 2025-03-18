from pages.base_paged import BrowserAutomation
from pages.locators import Locators
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


faker = Faker()


class NewOrderFooter(BrowserAutomation):
    def __init__(self, headless=True):
        super().__init__(headless)

    def click_footer_button(self):
        WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(Locators.BUTTON_FOOTER)
        ).click()

    def fill_form(self, name=None, email=None, phone=None, project=None):
        name = name or faker.name()
        email = email or faker.email()
        phone = phone or faker.phone_number()
        project = project or faker.sentence()

        self.browser.find_element(*Locators.INPUT_NAME_2).send_keys(name)
        self.browser.find_element(*Locators.INPUT_EMAIL_2).send_keys(email)
        self.browser.find_element(*Locators.INPUT_PHONE_2).send_keys(phone)
        self.browser.find_element(*Locators.INPUT_PROJECT_2).send_keys(project)

    def submit_form(self):
        WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)
        ).click()

    def validate_submission(self):
        try:
            # Ожидаем появления сообщения об успешной отправке
            success_message = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(Locators.CLOSE_BUTTON)
            )
            close_button = self.browser.find_element(*Locators.CLOSE_BUTTON)

            # Проверяем, что сообщение об успешной отправке видно
            if not success_message.is_displayed():
                raise Exception("Сообщение об успешной отправке не найдено!")

            # Закрываем форму
            close_button.click()

        except Exception as e:
            print(f"Ошибка при валидации формы: {e}")
            raise

    def close_form(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(Locators.CLOSE_BUTTON)
        ).click()
