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

    # Switch to the alert and close alert
    driver.switch_to.alert.accept()

    # Click to the Cart
    driver.find_element(By.XPATH, "//a[@id='cartur']").click()
    time.sleep(5)

    # assert that we redirected to the cart page
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='Products']").is_displayed()

    # validate item in the list
    assert driver.find_element(By.XPATH, "//td[normalize-space()='Samsung galaxy s6']").is_displayed()

    # Click to the Place Order
    driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
    time.sleep(5)

    assert driver.find_element(By.ID, "orderModalLabel").is_displayed()

    # Checkout Cart

    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Test")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Pune")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='card']").send_keys('123456789632')
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='month']").send_keys("March")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='year']").send_keys('2024')
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[normalize-space()='Purchase']").click()
    time.sleep(5)

    driver.save_screenshot('Order_confirmation.png')
    # Assert that the order is confirmed
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your purchase!']").is_displayed()

    order_confirmation = driver.find_element(By.XPATH, "//div[contains(@class,'showSweetAlert visible')]")

    if order_confirmation == True:
        print("Order Placed Sucessfully")
    else:
        print("Order Pending")
