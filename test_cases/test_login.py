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


def test_login_with_valid_data(setup):
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

    # Capture the element to verify that the user is logged in successfully
    welcome = driver.find_element(By.XPATH, "//a[@id='nameofuser']")

    # Validate that the user is logged in successfully
    if welcome.is_displayed():
        print("Login successfully")
    else:
        print("Login Failed")


def test_login_with_invalid_data(setup):
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
    username.send_keys("785%$$%tels")
    time.sleep(2)

    # Enter Password
    password = driver.find_element(By.XPATH, "//input[@id='loginpassword']")
    password.send_keys("admin@123")
    time.sleep(2)

    # Click to the Log in button
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
    login_button.click()
    time.sleep(5)

    # Switch to the alert and capture the value
    alert = driver.switch_to.alert
    alert_text = alert.text

    # Validate that user should not able to login with invalid inputs
    time.sleep(5)
    if alert_text == "User does not exist.":
        print("Test Case Passed")
    else:
        print('Test Case failed')

    # Close alert
    alert.accept()
