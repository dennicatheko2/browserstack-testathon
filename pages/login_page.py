from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_username(self, username):
        self.wait.until(EC.element_to_be_clickable((By.ID, "username"))).click()
        self.wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(@id,'react-select-2-option') and text()='{username}']")
        )).click()
        

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable((By.ID, "password"))).click()
        self.wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(@id,'react-select-3-option') and text()='{password}']")
        )).click()
        

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()
        

    def login(self, username, password):
        self.select_username(username)
        self.enter_password(password)
        self.submit()