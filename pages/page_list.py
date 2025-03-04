from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EnumerationElements:
    def __init__(self, browser):
        self.browser = browser
        self.elements_to_check = {
            "Ресторан": ("Разработка сайтов для ресторанов", "h1"),
            "Авто": ("Сайты для автомобильных салонов", "h1"),
            "Недвижимость": ("Создание сайта для агентства недвижимости", "h1"),
            "Премиум": ("Премиальные сайты", "h1"),
            "Адаптив": ("Адаптивные сайты", "h1"),
            "Стройка": ("Разработка сайтов для строительных компаний", "h1"),
            "Ремонт": ("Разработка сайтов для ресторанов", "h1"),
            "Здоровье": ("Кейсы", "h1"),
            "Медицина": ("Сайт клиники", "h1"),
            "Бизнес": ("Что входит в услугу", "p"),
        }

    def click_elements_by_text(self, *texts):
        for text in texts:
            elements = WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, f"//a[contains(., '{text}')]"))
            )

            for element in elements:
                element.click()
                self.check_element(text)
                self.check_h1_exists()
                self.check_p_exists()
                self.browser.back()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//body"))
                )

    def check_element(self, text):
        expected_text, element_type = self.elements_to_check.get(text, (None, None))

        if expected_text:
            if element_type == "h1":
                element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//h1[contains(text(), '{expected_text}')]"))
                )
            elif element_type == "p":
                element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_text}')]"))
                )
            else:
                print(f"Неизвестный тип элемента для {text}")
                return

            assert element.text == expected_text, f"Неверный текст в {element_type}: {element.text}"
        else:
            print(f"Не найдено соответствие для элемента: {text}")

    def check_h1_exists(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
        except:
            print("Ошибка: h1 не найден на странице")

    def check_p_exists(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Что входит в услугу')]")
            ))
        except:
            print("Ошибка: 'Что входит в услугу' (p) не найден на странице")

    def enumerate_and_check(self):
        self.click_elements_by_text(*self.elements_to_check.keys())
