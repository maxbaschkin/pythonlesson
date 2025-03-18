from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from pages.base_paged import BrowserAutomation


class NewOrderButton(BrowserAutomation):

    def __init__(self, headless=True):
        super().__init__(headless)
        self.faker = Faker('ru_RU')

    def fill_and_submit_form(self):
        name = self.faker.name()
        email = self.faker.email()
        phone = self.faker.phone_number()
        project_desc = self.faker.text(max_nb_chars=50)

        self.browser.find_element(By.XPATH, self.INPUT_NAME).send_keys(name)
        self.browser.find_element(By.XPATH, self.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(By.XPATH, self.INPUT_PHONE).send_keys(phone)
        self.browser.find_element(By.XPATH, self.INPUT_PROJECT).send_keys(project_desc)

        submit_button = WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.SUBMIT_BUTTON))
        )
        submit_button.click()

    def check_success_message_and_close(self):
        success_message = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, self.SUCCESS_MESSAGE))
        )
        assert success_message is not None, "Сообщение об успешной отправке не появилось"

        close_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE_BUTTON))
        )
        assert close_button.is_displayed(), "Кнопка закрытия не видна"
        close_button.click()

    def test_order_process(self):
        self.browser.find_element(By.XPATH, self.BUTTON_HEADER).click()
        self.fill_and_submit_form()
        self.check_success_message_and_close()

        self.browser.find_element(By.XPATH, self.BUTTON_FOOTER).click()
        self.fill_and_submit_form()
        self.check_success_message_and_close()

    def close_browser(self):
        self.browser.quit()
