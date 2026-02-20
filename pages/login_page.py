from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_username(self, username):
        dropdown = Select(
            self.wait.until(EC.presence_of_element_located(self.USERNAME))
        )
        dropdown.select_by_visible_text(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def login(self, username, password):
        self.select_username(username)
        self.enter_password(password)
        self.submit()