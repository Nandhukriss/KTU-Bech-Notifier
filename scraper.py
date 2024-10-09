from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    except Exception as e:
        print(f"Error fetching announcements: {e}")
        b_tech_announcements = []
    finally:
        driver.quit()

    return b_tech_announcements
