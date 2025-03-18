from selenium.webdriver.common.by import By


class Locators:
    #Локаторы
    BUTTON_HEADER = (By.XPATH, "//button[@class='_button_1anfh_27 _button--dot_1anfh_237 _button--sm_1anfh_40']")
    BUTTON_FOOTER = (By.XPATH, "//button[@class='_button_1anfh_27 _button--lightWhite_1anfh_106 _button--md_1anfh_46 _button_1ru51_204']")
    INPUT_NAME =  (By.XPATH, "//input[@name='name' and @type='text']")
    INPUT_EMAIL = (By.XPATH, "//input[@name='email' and @type='email']")
    INPUT_PHONE = (By.XPATH, "//input[@name='phone' and @type='text']")
    INPUT_PROJECT = (By.XPATH, "//textarea[@placeholder='Напишите кратко о проекте']")
    INPUT_NAME_2 = (By.XPATH, "(//input[@name='name' and @type='text'])[2]")
    INPUT_EMAIL_2 = (By.XPATH, "(//input[@name='email' and @type='email'])[2]")
    INPUT_PHONE_2 = (By.XPATH, "(//input[@name='phone' and @type='text'])[2]")
    INPUT_PROJECT_2 = (By.XPATH, "(//textarea[@placeholder='Напишите кратко о проекте'])[2]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Отправить')]")
    SUCCESS_MESSAGE = (By.XPATH, "//span[contains(text(), 'Заявка оформлена!')]")
    #// div[contains( @class , '_formWrapper_') and contains( @ class, '_Success_')]
    CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, '_closeForm_')]")
    PLACEHOLDER_FOOTER  = (By.XPATH, "//textarea[@placeholder='Напишите кратко о проекте']")
    SUBMIT_BUTTON_2 = (By.XPATH, "//button[@type='submit' and contains(text(), 'Обсудить проект')]")
    BUTTONS_TAGS = [
        (By.CSS_SELECTOR, "div._tagsWrapper_1r0gr_27 button:nth-of-type(1)"),
         (By.CSS_SELECTOR, "div._tagsWrapper_1r0gr_27 button:nth-of-type(2)"),
        (By.CSS_SELECTOR, "div._tagsWrapper_1r0gr_27 button:nth-of-type(3)"),
        (By.CSS_SELECTOR, "div._tagsWrapper_1r0gr_27 button:nth-of-type(4)"),
        (By.CSS_SELECTOR, "div._tagsWrapper_1r0gr_27 button:nth-of-type(5)"),
        (By.CSS_SELECTOR, "div._tagsWrapper_1r0gr_27 button:nth-of-type(6)")
        ]

# class Locators:
#     # Локаторы
#     BUTTON_HEADER = (By.CSS_SELECTOR, "button._button_1anfh_27._button--dot_1anfh_237._button--sm_1anfh_40")
#     BUTTON_FOOTER = (By.CSS_SELECTOR, "button._button_1anfh_27._button--lightWhite_1anfh_106._button--md_1anfh_46._button_1ru51_204")
#     INPUT_NAME = (By.CSS_SELECTOR, "input[name='name'][type='text']")
#     INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='email'][type='email']")
#     INPUT_PHONE = (By.CSS_SELECTOR, "input[name='phone'][type='text']")
#     INPUT_NAME_2 = (By.CSS_SELECTOR, "input[name='name'][type='text']:nth-of-type(2)")
#     INPUT_EMAIL_2 = (By.CSS_SELECTOR, "input[name='email'][type='email']:nth-of-type(2)")
#     INPUT_PHONE_2 = (By.CSS_SELECTOR, "input[name='phone'][type='text']:nth-of-type(2)")
#     INPUT_PROJECT_2 = (By.CSS_SELECTOR, "textarea[placeholder='Напишите кратко о проекте']:nth-of-type(2)")
#     SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']:contains('Отправить')")
#     SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div._formWrapper_1chag_94._Success_1chag_178")
#     CLOSE_BUTTON = (By.CSS_SELECTOR, "div._closeForm_1chag_214")
#     PLACEHOLDER_FOOTER = (By.CSS_SELECTOR, "textarea[placeholder='Напишите кратко о проекте']")
#     SUBMIT_BUTTON_2 = (By.CSS_SELECTOR, "button[type='submit']:contains('Обсудить проект')")

