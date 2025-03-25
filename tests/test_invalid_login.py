import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("locked_out_user", "secret_sauce"),
    ("invalid_user", "invalid_pass"),
    ("", ""),
])
def test_invalid_login(browser, username, password):
    page = LoginPage(browser)
    page.login(username, password)
    error = browser.find_element("css selector", "[data-test='error']")
    assert error.is_displayed()
