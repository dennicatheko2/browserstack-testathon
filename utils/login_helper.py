from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def login(driver, username, password):
    username_dropdown = Select(driver.find_element(By.ID, "username"))
    password_dropdown = Select(driver.find_element(By.ID, "password"))

    username_dropdown.select_by_visible_text(username)
    password_dropdown.select_by_visible_text(password)

    driver.find_element(By.ID, "login-btn").click()