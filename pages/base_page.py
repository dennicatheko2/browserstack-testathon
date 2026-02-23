from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class BasePage:
    FIRST_ADD_TO_CART = (
        By.XPATH, '//*[@id="1"]/div[4]'
    )

    # Vendor filter XPaths 
    VENDOR_FILTERS = {
        "apple": (By.XPATH, "//*[@id='__next']/div/div/main/div[1]/div[1]/label/span"),
        "samsung": (By.XPATH, "//*[@id='__next']/div/div/main/div[1]/div[2]/label/span"),
        "google": (By.XPATH, "//*[@id='__next']/div/div/main/div[1]/div[3]/label/span"),
        "oneplus": (By.XPATH, "//*[@id='__next']/div/div/main/div[1]/div[4]/label/span"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

   
    def add_first_item_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_ADD_TO_CART)
        ).click()


    # Locator for product cards (adjust only if needed)
    PRODUCT_TITLES = (By.CSS_SELECTOR, "[data-testid='product-name']")

    def click_vendor_filter(self, vendor: str):
        vendor = vendor.lower()
        assert vendor in self.VENDOR_FILTERS, f"Vendor '{vendor}' not supported"

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VENDOR_FILTERS[vendor])
        ).click()

    def get_all_product_titles(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_TITLES)
        )
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [el.text.lower() for el in elements]