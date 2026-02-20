import os
from pages.home_page import HomePage

def test_homepage_loads(driver):
    base_url = os.getenv("BASE_URL")
    home = HomePage(driver)

    home.open(base_url)
    assert "sign in" in driver.page_source.lower()