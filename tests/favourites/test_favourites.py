import pytest
from utils.csv_reader import load_test_cases
from utils.login_helper import login

test_data = load_test_cases("Favourites")

@pytest.mark.parametrize("data", test_data)
def test_favourites(driver, data):
    login(driver, "fav_user", "testingsfun99")

    driver.find_element("id", "favourites").click()
    assert "favourites" in driver.current_url.lower()