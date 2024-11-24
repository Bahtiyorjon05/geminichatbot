from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium WebDriver (update the path to ChromeDriver)
driver = webdriver.Chrome(executable_path='path_to_your_chromedriver')  # Change this path

url = 'https://learn.inha.ac.kr/local/ubdoc/?id=1245093&tp=m&pg=ubfile'  # Replace with actual URL
driver.get(url)

# Wait for the page to fully load (adjust the wait time as necessary)
time.sleep(5)  # You can replace this with WebDriverWait if you prefer

# Extract the content (modify this based on the actual content you're looking for)
try:
    body = driver.find_element(By.TAG_NAME, 'body')  # Get the entire body text
    print(body.text)  # Print the body text
except Exception as e:
    print(f"Error extracting content: {e}")

# Close the browser
driver.quit()
