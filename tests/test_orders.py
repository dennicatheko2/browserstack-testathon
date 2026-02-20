import pytest
from utils.csv_reader import load_test_cases
from utils.login_helper import login

test_data = load_test_cases("Orders")

@pytest.mark.parametrize("data", test_data)
def test_orders(driver, data):
    login(driver, "existing_orders_user", "password123")

    driver.find_element("id", "orders").click()
    assert "orders" in driver.current_url.lower()