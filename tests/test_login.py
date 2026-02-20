import os
import pytest
from utils.csv_reader import read_test_data
from pages.home_page import HomePage
from pages.login_page import LoginPage

from dotenv import load_dotenv
import os

load_dotenv()  

BASE_URL = os.getenv("BASE_URL")
assert BASE_URL, "BASE_URL not set in .env"

def test_demo_user_can_login(driver):
    base_url = os.getenv("BASE_URL")
    assert base_url, "BASE_URL not set"

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open(base_url)
    home.click_sign_in()

    login.login("demouser", "testingsfun99")

    assert "logout" in driver.page_source.lower()

def test_locked_user_cannot_login(driver):
    base_url = os.getenv("BASE_URL")

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open(base_url)
    home.click_sign_in()

    login.login("locked_user", "testingsfun99")

    assert "Your account has been locked." in driver.page_source.lower()
    