from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_paged import BrowserAutomation
from pages.locators import Locators
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# faker = Faker()
#
# class PlaceholderFooter(BrowserAutomation):
#     def __init__(self, headless=True):
#         super().__init__(headless)
#
#     def generate_data(self, name=None, email=None, phone=None, project=None):
#         self.name = name or faker.name()
#         self.email = email or faker.email()
#         self.phone = phone or faker.phone_number()
#         self.project = project or faker.sentence()
#
#     def fill_form(self):
#         try:
#             print("Заполняю форму...")
#             WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(Locators.PLACEHOLDER_FOOTER)
#             ).send_keys(self.project)
#
#             WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(Locators.INPUT_NAME)
#             ).send_keys(self.name)
#
#             WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(Locators.INPUT_EMAIL)
#             ).send_keys(self.email)
#
#             WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(Locators.INPUT_PHONE)
#             ).send_keys(self.phone)
#
#         except (NoSuchElementException, TimeoutException) as e:
#             print(f"Ошибка при заполнении формы: {e}")
#             raise
#
#     def click_tags(self):
#         tags = [
#             "Разработка",
#             "Аналитика",
#             "Логотип",
#             "Продвижение",
#             "Фирменный стиль",
#             "Другое"
#         ]
#
#         for tag in tags:
#             try:
#                 xpath = f"//button[contains(@class, '_tagWrapper_1ctd8_27') and .//span[text()='{tag}']]"
#                 print(f"Кликаю по тегу: {tag}")
#                 tag_button = WebDriverWait(self.browser, 10).until(
#                     EC.element_to_be_clickable((By.XPATH, xpath))
#                 )
#                 tag_button.click()
#             except (NoSuchElementException, TimeoutException) as e:
#                 print(f"Ошибка при клике на тег '{tag}': {e}")
#                 raise
#
#     def submit_form(self):
#         try:
#             print("Нажимаю на кнопку отправки формы...")
#             submit_button = WebDriverWait(self.browser, 15).until(
#                 EC.visibility_of_element_located(Locators.SUBMIT_BUTTON_2)
#             )
#             submit_button.click()
#         except (NoSuchElementException, TimeoutException) as e:
#             print(f"Ошибка при нажатии на кнопку отправки формы: {e}")
#             raise
#
#     def validate_submission(self):
#         try:
#             success_message = WebDriverWait(self.browser, 20).until(
#                 EC.element_to_be_clickable(Locators.CLOSE_BUTTON)
#             )
#             close_button = self.browser.find_element(*Locators.CLOSE_BUTTON)
#
#             if not success_message.is_displayed():
#                 raise Exception("Сообщение об успешной отправке не найдено!")
#
#             close_button.click()
#
#         except Exception as e:
#             print(f"Ошибка при валидации формы: {e}")
#             raise
#
#     def close_form(self):
#         try:
#             WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(Locators.CLOSE_BUTTON)
#             ).click()
#             print("Форма закрыта.")
#         except (NoSuchElementException, TimeoutException) as e:
#             print(f"Ошибка при закрытии формы: {e}")
#             raise
#
#     def process_form(self, url):
#         try:
#             self.open_url(url)
#             self.generate_data()
#             self.fill_form()
#             self.click_tags()
#             self.submit_form()
#             self.validate_submission()
#             self.close_form()
#         except Exception as e:
#             print(f"Ошибка при обработке формы: {e}")
#             raise

faker = Faker()


class PlaceholderFooter(BrowserAutomation):
    def __init__(self, headless=True):
        super().__init__(headless)

    def generate_data(self, name=None, email=None, phone=None, project=None):
        self.name = name or faker.name()
        self.email = email or faker.email()
        self.phone = phone or faker.phone_number()
        self.project = project or faker.sentence()

    def fill_form(self):
        try:
            print("Заполняю форму...")
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(Locators.PLACEHOLDER_FOOTER)
            ).send_keys(self.project)

            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(Locators.INPUT_NAME)
            ).send_keys(self.name)

            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(Locators.INPUT_EMAIL)
            ).send_keys(self.email)

            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(Locators.INPUT_PHONE)
            ).send_keys(self.phone)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Ошибка при заполнении формы: {e}")
            raise

    def click_tags(self):
        for index, tag_locator in enumerate(Locators.BUTTONS_TAGS, start=1):
            try:
                print(f"Кликаю по тегу #{index}...")
                tag_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(tag_locator)
                )
                tag_button.click()
            except (NoSuchElementException, TimeoutException) as e:
                print(f"Ошибка при клике на тег #{index}: {e}")
                raise

    def submit_form(self):
        try:
            print("Нажимаю на кнопку отправки формы...")
            submit_button = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable(Locators.SUBMIT_BUTTON_2)
            )
            submit_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Ошибка при нажатии на кнопку отправки формы: {e}")
            raise

    def validate_submission(self):
        try:
            success_message = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable(Locators.CLOSE_BUTTON)
            )
            close_button = self.browser.find_element(*Locators.CLOSE_BUTTON)

            if not success_message.is_displayed():
                raise Exception("Сообщение об успешной отправке не найдено!")

            close_button.click()
        except Exception as e:
            print(f"Ошибка при валидации формы: {e}")
            raise

    def close_form(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(Locators.CLOSE_BUTTON)
            ).click()
            print("Форма закрыта.")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Ошибка при закрытии формы: {e}")
            raise

    def process_form(self, url):
        try:
            self.open_url(url)
            self.generate_data()
            self.fill_form()
            self.click_tags()
            self.submit_form()
            self.validate_submission()
            self.close_form()
        except Exception as e:
            print(f"Ошибка при обработке формы: {e}")
            raise
