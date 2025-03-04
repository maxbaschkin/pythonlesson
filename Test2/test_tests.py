from Page.main_page import MainPage

def test_order_form_headers():
    main = MainPage(browser)
    main.open()
    assert main.text_is_displayed()
    