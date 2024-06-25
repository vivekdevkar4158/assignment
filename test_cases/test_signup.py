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


def test_sign_up(setup):
    driver = setup
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Navigate to the Sign Up form
    driver.find_element(By.XPATH, "//a[@id='signin2']").click()
    time.sleep(5)

    # Assert that the Sign Up form opened
    assert driver.find_element(By.ID, "signInModalLabel").is_displayed()

    # Enter Username
    username = driver.find_element(By.XPATH, "//input[@id='sign-username']")
    username.send_keys("admintest789@gmail.com")

    time.sleep(5)

    # Enter Password
    password = driver.find_element(By.XPATH, "//input[@id='sign-password']")
    password.send_keys("admin@123")

    # Click Sign Up button
    signup_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']")
    signup_button.click()

    time.sleep(5)

    # Switch to the alert and capture the value
    alert = driver.switch_to.alert
    alert_text = alert.text

    # Validate that Sign up successfully done
    time.sleep(5)
    if alert_text == "Sign up successful.":
        print("Sign up Successful")
    else:
        print('Sign up failed')

    # Close alert
    alert.accept()


def test_sign_up_with_invalid_data(setup):
    driver = setup
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Navigate to the Sign Up form
    driver.find_element(By.XPATH, "//a[@id='signin2']").click()
    time.sleep(5)

    # Assert that the Sign Up form opened
    assert driver.find_element(By.ID, "signInModalLabel").is_displayed()

    # Enter Username
    username = driver.find_element(By.XPATH, "//input[@id='sign-username']")
    username.send_keys("admintest789@gmail.com")

    time.sleep(5)

    # Enter Password
    password = driver.find_element(By.XPATH, "//input[@id='sign-password']")
    password.send_keys("admin@123")

    # Click Sign Up button
    signup_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']")
    signup_button.click()

    time.sleep(5)

    # Switch to the alert and capture the value
    alert = driver.switch_to.alert
    alert_text = alert.text

    # Validate that Sign up successfully done
    time.sleep(5)
    if alert_text == "This user already exist.":
        print("Test Case Passed: User is not able to Sign up with existing data")
    else:
        print('Sign up possible for existing data')

    # Close alert
    alert.accept()
