from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME = (By.ID, "firstNameInput")
    LAST_NAME = (By.ID, "lastNameInput")
    ADDRESS = (By.ID, "addressLine1Input")
    STATE = (By.ID, "provinceInput")
    POSTAL = (By.ID, "postCodeInput")
    SUBMIT_BTN = (By.ID, "checkout-shipping-continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self, first, last, address, state, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.POSTAL).send_keys(postal)

    def submit_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BTN)
        ).click()