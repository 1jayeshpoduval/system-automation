from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Login
    driver.get("https://ecommerce-playground.lambdatest.io/")

    my_account = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My account"))
    )
    my_account.click()

    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()

    driver.find_element(By.ID, "input-email").send_keys("testuser001@example.com")
    driver.find_element(By.ID, "input-password").send_keys("TestPass123!")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    time.sleep(2)

    # Navigate to Order History
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/order")

    time.sleep(2)

    # Check for orders or no orders message
    page_content = driver.find_element(By.TAG_NAME, "body").text

    if "No results" in page_content:
        print("TEST PASSED: Order History page displays correctly (no orders)")
    elif "Order ID" in page_content:
        print("TEST PASSED: Order History page displays orders")
    else:
        print("TEST FAILED: Order History page content unexpected")

    time.sleep(2)

finally:
    driver.quit()
