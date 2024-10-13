import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from logger_config import logger

# Chrome options setup
chrome_options = Options()
chrome_options.add_argument("--headless=old")  # Headless mode

async def fetch_announcements():
    """Fetches the current announcements from the KTU website."""
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://ktu.edu.in/menu/announcements")

        latest_announcements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.p-t-15.p-b-15.shadow.row.m-b-25.row'))
        )

        # Extract and return B.Tech related announcements
        b_tech_announcements = [announcement.text for announcement in latest_announcements if "B.Tech" in announcement.text]
        # Extract and return B.Tech related results
        driver.get("https://ktu.edu.in/exam/result")
        # Wait for the page to load and locate the dropdown by its class name or other locators
        dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-select-sm"))
        )

        # Use WebDriverWait to wait until the B.Tech option becomes available in the dropdown
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//option[text()='B.Tech']"))
            )
            # Now interact with the dropdown
            select = Select(dropdown)
            select.select_by_visible_text("B.Tech")
        except Exception as e :
            return b_tech_announcements 
        
        time.sleep(5)

        # Wait for either the 'NO RECORDS FOUND' message or the results to appear
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'NO RECORDS FOUND')]"))
            )
        except TimeoutException:
            # No 'NO RECORDS FOUND' message, proceed with fetching the results
            b_tech_results = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.border-bottom-dotted.p-b-5.p-t-5.row'))
            )
            b_tech_results_text = [result.text for result in b_tech_results]

            # Append B.Tech results to the announcements list
            b_tech_announcements.extend(b_tech_results_text)

    except Exception as e:
        logger.error(f"Error fetching announcements: {e}")
        b_tech_announcements = []
    finally:
        driver.quit()

    return b_tech_announcements

