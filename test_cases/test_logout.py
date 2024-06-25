import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_process(setup):
    driver = setup
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)


def test_logout(setup):
    driver = setup
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Navigate to the Log in form
    driver.find_element(By.XPATH, "//a[@id='login2']").click()
    time.sleep(2)

    # Assert that the Log in form opened
    assert driver.find_element(By.XPATH, "//h5[@id='logInModalLabel']").is_displayed()
    time.sleep(2)

    # Enter Username
    username = driver.find_element(By.XPATH, "//input[@id='loginusername']")
    username.send_keys("admintest123@gmail.com")
    time.sleep(2)

    # Enter Password
    password = driver.find_element(By.XPATH, "//input[@id='loginpassword']")
    password.send_keys("admin@123")
    time.sleep(2)

    # Click to the Log in button
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
    login_button.click()
    time.sleep(5)

    # assertion for logged in successfully
    assert driver.find_element(By.XPATH, "//a[@id='nameofuser']").is_displayed()

    # Click on the logout
    driver.find_element(By.ID, "logout2").click()

    if (driver.find_element(By.ID, "login2").is_displayed()):
        print("Test Case Passed: User is able to logout successfully")


