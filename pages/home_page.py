from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    SIGN_IN = (By.ID, "Sign In")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN)).click()