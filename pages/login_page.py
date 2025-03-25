class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.browser.find_element("id", "user-name").clear()
        self.browser.find_element("id", "user-name").send_keys(username)
        self.browser.find_element("id", "password").clear()
        self.browser.find_element("id", "password").send_keys(password)
        self.browser.find_element("id", "login-button").click()
