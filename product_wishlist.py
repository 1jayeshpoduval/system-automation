from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Login first
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
    time.sleep(3)

    # Search for Samsung product
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Samsung SyncMaster")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Click on first product
    first_product = driver.find_element(By.CLASS_NAME, "product-thumb")
    product_link = first_product.find_element(By.TAG_NAME, "a")
    product_link.click()
    time.sleep(3)

    # Add to wishlist
    wishlist_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to Wish List']"))
    )
    wishlist_btn.click()

    # Wait for success message
    time.sleep(3)

    # Navigate to wishlist
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist")

    # Verify product in wishlist
    wishlist_items = driver.find_elements(By.CLASS_NAME, "table-responsive")

    if len(wishlist_items) > 0:
        print("TEST PASSED: Product successfully added to wishlist")
    else:
        print("TEST FAILED: Product not found in wishlist")

    time.sleep(3)

finally:
    driver.quit()
