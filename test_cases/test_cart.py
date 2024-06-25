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


def test_add_to_cart(setup):
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
    time.sleep(10)

    # click on the product
    driver.find_element(By.XPATH, "//a[normalize-space()='Samsung galaxy s6']").click()
    time.sleep(5)
    # assert that the product is opened
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='Samsung galaxy s6']").is_displayed()
    time.sleep(2)
    # assert that the Add to cart button is available on product page
    assert driver.find_element(By.XPATH, "//a[normalize-space()='Add to cart']").is_displayed()
    time.sleep(5)

    # Click on the Add to cart button
    driver.find_element(By.XPATH, "//a[normalize-space()='Add to cart']").click()

    time.sleep(5)

    # Switch to the alert and capture the value
    alert = driver.switch_to.alert
    alert_text = alert.text

    # Validate that the product is added to the cart successfully
    if alert_text == "Product added.":
        print("Product added to the Cart")
    else:
        print('Product is not added to the Cart')

    # Close alert
    alert.accept()
