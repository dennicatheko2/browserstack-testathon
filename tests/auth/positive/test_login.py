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

def test_demo_user_can_login(driver):
    login = LoginPage(driver)
    login.login("demouser", "testingisfun99")

    WebDriverWait(driver, 10).until(EC.url_to_be("https://testathon.live/?signin=true"))
    assert driver.current_url == "https://testathon.live/?signin=true"

def test_locked_user_cannot_login(driver):
    login = LoginPage(driver)
    login.login("locked_user", "testingisfun99")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your account has been locked.')]"))
    )
    assert "Your account has been locked." in driver.page_source

def test_image_cannot_load_user_login(driver):
    login = LoginPage(driver)
    login.login("image_not_loading_user", "testingisfun99")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    images = driver.find_elements(By.TAG_NAME, "img")
    broken_images = [
        img for img in images
        if driver.execute_script("return arguments[0].naturalWidth", img) == 0
    ]
    assert len(broken_images) > 0, "Expected broken images but all images loaded successfully" 
   
def test_existing_orders_user_login(driver):
    login = LoginPage(driver)
    login.login("existing_orders_user", "testingisfun99")

    WebDriverWait(driver, 10).until(EC.url_to_be("https://testathon.live/?signin=true"))
    assert driver.current_url == "https://testathon.live/?signin=true"

def test_fav_user_login(driver):
    login = LoginPage(driver)
    login.login("fav_user", "testingisfun99")

    WebDriverWait(driver, 10).until(EC.url_to_be("https://testathon.live/?signin=true"))
    assert driver.current_url == "https://testathon.live/?signin=true"