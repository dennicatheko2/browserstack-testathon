import pytest
from utils.csv_reader import load_test_cases
from utils.login_helper import login

test_data = load_test_cases("Checkout")

@pytest.mark.parametrize("data", test_data)
def test_checkout(driver, data):
    login(driver, "demoUser", "password123")

    driver.find_element("css selector", ".add-to-cart").click()
    driver.find_element("id", "checkout").click()

    assert "checkout" in driver.current_url.lower()