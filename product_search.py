from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

search_terms = ["MacBook", "iPod", "Canon", "Samsung"]
expected_counts = [3, 5, 2, 2]

try:
    driver.get("https://ecommerce-playground.lambdatest.io/")

    for i, search_term in enumerate(search_terms):
        # Locate search bar
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(4)

        # Count results
        results = driver.find_elements(By.CLASS_NAME, "product-thumb")
        result_count = len(results)

        print(f"Search '{search_term}': Found {result_count} results (Expected: {expected_counts[i]})")

        if result_count >= expected_counts[i]:
            print(f"Search test for '{search_term}' PASSED")
        else:
            print(f"Search test for '{search_term}' FAILED")

        # Navigate back to homepage for next search
        driver.get("https://ecommerce-playground.lambdatest.io/")
        time.sleep(2)

    print("\nAll search tests completed")

finally:
    driver.quit()
