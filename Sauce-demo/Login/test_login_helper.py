from selenium.webdriver.common.by import By

class LoginHelper:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username="standard_user", password="secret_sauce"):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_logged_in(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "title").is_displayed()
        except:
            return False

    def ensure_logged_in(self):
        if not self.is_logged_in():
            print("Session expired. Logging in again.")
            self.login()