import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd

# Setup Selenium WebDriver with Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU (for headless mode)
chrome_options.add_argument("--window-size=1920x1080")  # Set window size for scraping

driver = webdriver.Chrome(options=chrome_options)

# Open eBay tech deals page
driver.get("https://www.ebay.com/globaldeals/tech")

# Wait for the page to load and scroll to trigger lazy loading
time.sleep(3)  # Wait for initial content to load

# Scroll down to the bottom to load all products (Lazy loading trigger)
scroll_pause_time = 2  # seconds
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    
    # Calculate new scroll height and compare with last height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Extract product details
products = driver.find_elements(By.CSS_SELECTOR, ".dne-itemtile")  # The outer wrapper for each product
product_data = []

for product in products:
    try:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get product title
        title_element = product.find_element(By.CSS_SELECTOR, ".dne-itemtile-title")
        title = title_element.text
        
        # Get discounted price
        price_element = product.find_element(By.CSS_SELECTOR, "[itemprop='price']")
        price = price_element.text
        
        # Get product URL
        item_url = product.find_element(By.CSS_SELECTOR, "a[itemprop='url']").get_attribute("href")
        
        # Hotness Status (if available)
        hotness_status = None
        try:
            hotness_status = product.find_element(By.CSS_SELECTOR, ".dne-itemcard-hotness").text
        except:
            hotness_status = None
        
        # Append the product data
        product_data.append([timestamp, title, price, hotness_status, item_url])
    
    except Exception as e:
        print(f"Error extracting data for a product: {e}")
        continue

# Save data to CSV
file_name = "ebay_tech_deals.csv"
header = ["timestamp", "title", "price", "hotness_status", "item_url"]

# Check if the file already exists, and append data if it does
try:
    existing_data = pd.read_csv(file_name)
    new_data = pd.DataFrame(product_data, columns=header)
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    combined_data.to_csv(file_name, index=False)
except FileNotFoundError:
    # If the file doesn't exist, create a new one and save the data
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(product_data)

# Close the browser
driver.quit()
