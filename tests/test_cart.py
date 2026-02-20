import pytest
from utils.csv_reader import load_test_cases
from utils.login_helper import login

test_data = load_test_cases("Cart")

@pytest.mark.parametrize("data", test_data)
def test_cart(driver, data):
    login(driver, "demoUser", "password123")

    # Example add to cart
    driver.find_element("css selector", ".add-to-cart").click()

    driver.find_element("id", "cart").click()
    assert "cart" in driver.current_url.lower()