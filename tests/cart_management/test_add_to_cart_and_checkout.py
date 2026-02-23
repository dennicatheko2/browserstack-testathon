import os
import pytest
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()

@pytest.mark.cart
@pytest.mark.critical
def test_user_can_checkout_successfully(driver):
    base_url = os.getenv("BASE_URL")

    home = HomePage(driver)
    login = LoginPage(driver)
    catalog = BasePage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Open site
    home.open(base_url)
    home.click_sign_in()

    # Login
    login.login("demouser", "testingisfun99")

    # Add item & checkout
    catalog.add_first_item_to_cart()
    cart.click_checkout()

    # 🔥 Generate fake checkout data
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_address()
    state = fake.state()
    postal = fake.postcode()

    # Fill checkout form
    checkout.fill_checkout_form(
        first=first_name,
        last=last_name,
        address=address,
        state=state,
        postal=postal
    )

    checkout.submit_order()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Your Order has been successfully placed')]")
        )
    )

    assert "Your Order has been successfully placed" in driver.page_source