from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    HEADER_BUTTON_SELECTOR = "(//button[@class='_button_1anfh_27 _button--dot_1anfh_237 _button--sm_1anfh_40'])"
    FOOTER_BUTTON_SELECTOR = "(//button[@class='_button_1anfh_27 _button--lightWhite_1anfh_106 _button--md_1anfh_46 _button-custom_17yka_470'])"
    SUBMIT_BUTTON_SELECTOR = 'button._button_1anfh_27._button--violet_1anfh_58._button--lg_1anfh_52._custom-button_1uhw6_321'
    CHAT_BUTTON_SELECTOR = "div.ws-btn-title"
    MESSAGE_INPUT_SELECTOR = "//div[@class='ws-textarea']"
    FORM_INPUTS = {
        'name': "(//input[@name='name' and @type='text'])[2]",
        'email': "(//input[@name='email' and @type='email'])[2]",
        'phone': "(//input[@name='phone' and @type='text'])[2]",
        'message': "(//textarea[@placeholder='Напишите кратко о проекте'])[2]"
    }

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://preprod.softmg.ru/')

    def fill_form(self, form_data):
        self.browser.find_element(By.XPATH, self.FORM_INPUTS['name']).send_keys(form_data['name'])
        self.browser.find_element(By.XPATH, self.FORM_INPUTS['email']).send_keys(form_data['email'])
        self.browser.find_element(By.XPATH, self.FORM_INPUTS['phone']).send_keys(form_data['phone'])
        self.browser.find_element(By.XPATH, self.FORM_INPUTS['message']).send_keys(form_data['message'])

    def click_submit(self):
        submit_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.SUBMIT_BUTTON_SELECTOR))
        )
        submit_button.click()

    def click_chat(self):
        chat_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.CHAT_BUTTON_SELECTOR))
        )
        chat_button.click()

    def send_message(self, message):
        message_input = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.MESSAGE_INPUT_SELECTOR))
        )
        message_input.send_keys(message)
        self.browser.find_element(By.CSS_SELECTOR, ".ws-textarea-send-btn[title='Отправить']").click()

    def fill_chat_form(self, name, phone, email):
        name_input = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ws-preform-input.ws-preform-name"))
        )
        name_input.send_keys(name)
        self.browser.find_element(By.CSS_SELECTOR,
                                  ".ws-preform-input.ws-preform-phone.ws-phone-codes-target-input").send_keys(phone)
        self.browser.find_element(By.CSS_SELECTOR, ".ws-preform-input.ws-preform-email").send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, ".ws-preform-btn.ws-preform-btn-save").click()
