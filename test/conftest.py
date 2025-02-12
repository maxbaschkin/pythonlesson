import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def logo_selector():
    return "svg._logoSMG_kdgsi_137"


@pytest.fixture
def click_button_and_logo():
    def _click_button_and_logo(browser, button_xpath, logo_selector):
        button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        button.click()
        logo = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, logo_selector))
        )
        logo.click()

    return _click_button_and_logo


@pytest.fixture
def hrefs_test_6_1():
    return [
        '/examples/restoran/',
        '/examples/auto/',
        '/examples/nedvigimost/',
        '/examples/premium/',
        '/examples/adaptiv/',
        '/examples/bizness/',
        '/examples/stroitelnie-kompanyy/',
        '/examples/?tag=health/',
        '/examples/med-klinika/'
    ]


@pytest.fixture
def hrefs_test_6_2():
    return [
        '/examples/alpfederation/',
        '/examples/internet_magazin-campioshop/',
        '/examples/vitobox_servis_po_podboru_vitaminov_na_osnove_umnogo_algoritma/',
        '/examples/rosnano/',
        '/examples/servis_informatsionnoy_bezopasnosti/',
        '/examples/tonkiy_i_partnery_uslugi_bukhgalterskogo_i_yuridicheskogo_autsorsinga/'
    ]


@pytest.fixture
def hrefs_test_6_3():
    return [
        '/development/',
        '/ga/',
        '/promotion/',
        '/development/seo/',
        '/dorabotka-saytov/',
        '/support/',
        '/application-development/'
    ]


@pytest.fixture
def hrefs_test_7():
    return [
        '/development/framework/javascript/',
        '/development/yii/',
        '/development/zend/',
        '/development/framework/java/',
        '/development/laravel/',
        '/development/codeigniter/',
        '/development/symfony/',
        '/development/drupal/',
        '/development/shop/virtuemart/',
        '/development/shop/opencart/',
        '/development/wordpress/',
        '/development/shop/wordpress/',
        '/development/shop/ubercart/',
        '/development/joomla/',
        '/development/shop/1c-bitrix/',
        '/development/shop/magento/',
        '/development/shop/prestashop/',
        '/development/shop/oscommerce/',
        '/development/netcat/',
        '/development/umicms/',
        '/development/shop/shopscript/',
        '/application-development/ios/',
        '/support/wordpress/',
        '/development/wix/',
        '/support/bitrix/',
        '/development/cakephp/'
    ]
