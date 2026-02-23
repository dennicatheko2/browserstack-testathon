import os
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage

@pytest.mark.catalog
@pytest.mark.filter
@pytest.mark.critical
@pytest.mark.parametrize(
    "vendor",
    ["Samsung", "Apple", "Google", "OnePlus"]
)
def test_filter_by_vendor_shows_correct_products(driver, vendor):
    base_url = os.getenv("BASE_URL")

    home = HomePage(driver)
    login = LoginPage(driver)
    catalog = BasePage(driver)

    # Open site
    home.open(base_url)
   
    # Click vendor filter
    catalog.click_vendor_filter(vendor)

    # Get displayed vendors
    displayed_vendors = catalog.get_displayed_vendors()

    assert displayed_vendors, "No products displayed after filtering"

    for product_vendor in displayed_vendors:
        assert vendor.lower() in product_vendor, (
            f"Expected vendor '{vendor}' but found '{product_vendor}'"
        )