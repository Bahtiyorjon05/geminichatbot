from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ Open Ziyouz.com
driver.get("https://ziyouz.uz/")
print("✅ Opened Ziyouz.com successfully.")

try:
    # ✅ Wait for the page to load fully
    time.sleep(3)

    # ✅ Check if the search box is inside an iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if iframes:
        driver.switch_to.frame(iframes[0])  # Switch to the first iframe if found
        print("🔄 Switched to iframe.")

    # ✅ Wait until the search box is visible
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'search-field')]"))
    )

    # ✅ Use JavaScript to ensure it's visible
    driver.execute_script("arguments[0].scrollIntoView();", search_box)

    # ✅ Enter search query
    search_query = "Imom"  # Change this to any book title
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    print(f"✅ Searching for: {search_query}")

    # ✅ Wait for search results to load
    time.sleep(5)

    # ✅ Extract book links
    book_links = []
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        href = link.get_attribute("href")
        if href and "ziyouz.uz" in href:
            book_links.append(href)

    print(f"✅ Found {len(book_links)} book links.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
