import os
import pytest
from selenium.webdriver.common.by import By
from utils.csv_reader import read_test_data
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(autouse=True)
def navigate_to_login(driver):
    home = HomePage(driver)
    driver.maximize_window()
    home.open(os.getenv("BASE_URL"))
    home.click_sign_in()

def test_login_with_empty_fields(driver):
    login = LoginPage(driver)
    login.submit()
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid Username')]"))
    )
    assert "Invalid Username" in driver.page_source

def test_with_empty_password(driver):
    login = LoginPage(driver)
    login.login("demouser", "")

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid Password')]"))
    )
    assert "Invalid Password" in driver.page_source

def test_with_empty_username(driver):
    login = LoginPage(driver)
    login.login("", "testingisfun99")

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid Username')]"))
    )
    assert "Invalid Username" in driver.page_source


#Not really necessary in our case since the isername is Coded in a dropdown
def test_with_incorrect_username(driver):
    login = LoginPage(driver)
    login.login("demouser", "IncorrectPassword")

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid Password)]"))
    )
    assert "Invalid Password" in driver.page_source

