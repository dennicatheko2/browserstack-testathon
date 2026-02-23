from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CHECKOUT_BTN = (
        By.XPATH,
        '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]/div[3]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        ).click()