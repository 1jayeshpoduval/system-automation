from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 # Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
try:
 # Navigate to homepage
    driver.get("https://ecommerce-playground.lambdatest.io/")
 # Click My Account dropdown
    my_account = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My account")))
    my_account.click()
 # Click Register link
    register_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
 )
    register_link.click()
 # Fill registration form
    driver.find_element(By.ID, "input-firstname").send_keys("Michael")
    driver.find_element(By.ID, "input-lastname").send_keys("Jordan")
    driver.find_element(By.ID, "input-email").send_keys("testuser002@example.com")
    driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    driver.find_element(By.ID, "input-password").send_keys("TestPass123!")
    driver.find_element(By.ID, "input-confirm").send_keys("TestPass123!")
 # Select newsletter subscription
    driver.find_element(By.CSS_SELECTOR, "label[for='input-newsletter-yes']").click()
 # Accept privacy policy
    driver.find_element(By.CSS_SELECTOR, "label[for='input-agree']").click()
 # Click Continue button
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
 # Verify success message
    success_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
 )
    
    if "Your Account Has Been Created!" in success_msg.text:
        print("TEST PASSED: Registration successful")
    else:
        print("TEST FAILED: Success message not found")
    
    time.sleep(5)
    
finally:
    driver.quit()