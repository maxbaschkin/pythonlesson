from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Asserts:
    def __init__(self, browser):
        self.browser = browser

    def assert_success_message(self, message_text):
        #Проверка успешной отправки формы.
        success_message = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span._typography_1f6lr_28._typography--h5_1f6lr_134"))
        )
        assert success_message.text == message_text, f"Ожидаемое сообщение: {message_text}, получено: {success_message.text}"

    def assert_message_sent(self, message_xpath):
        #Проверка, что сообщение отправлено в чат.
        sent_message = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, message_xpath))
        )
        assert sent_message.is_displayed(), "Сообщение не было отправлено!"

    def assert_element_visible(self, element_locator, locator_type=By.CSS_SELECTOR):
        #Проверка видимости элемента.
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((locator_type, element_locator))
        )
        assert element.is_displayed(), f"Элемент {element_locator} не отображается!"

    def assert_page_transition(self, page_header_locator):
        #Проверка успешности перехода на новую страницу.
        page_header = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, page_header_locator))
        )
        assert page_header.is_displayed(), "Переход по вкладке не был успешным!"

    def assert_logo_visible(self, logo_locator):
        #Проверка, что логотип отображается на главной странице.
        logo = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, logo_locator))
        )
        assert logo.is_displayed(), "Логотип не найден на главной странице!"
