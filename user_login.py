from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to homepage
    driver.get("https://ecommerce-playground.lambdatest.io/")

    # Click My Account dropdown
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My account"))
    )
    my_account.click()

    # Click Login link
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()

    # Enter credentials
    driver.find_element(By.ID, "input-email").send_keys("testuser001@example.com")
    driver.find_element(By.ID, "input-password").send_keys("TestPass123!")

    # Click Login button
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    # Verify login success by checking URL
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/account")
    )

    # Verify account heading
    account_heading = driver.find_element(By.TAG_NAME, "h2")
    if "My Account" in account_heading.text:
        print("TEST PASSED: Login successful")
    else:
        print("TEST FAILED: Login verification failed")

    time.sleep(5)

finally:
    driver.quit()
