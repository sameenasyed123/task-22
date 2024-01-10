from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://www.instagram.com/guviofficial/"
driver.get(url)

try:
    # Wait for the page to load
    time.sleep(5)

    # Locate the followers count
    followers_count_element = driver.find_element(By.XPATH, "//span[@class='g47SY ']")
    followers_count = followers_count_element.text

    # Locate the following count
    following_count_element = driver.find_element(By.XPATH, "(//span[@class='g47SY '])[3]")
    following_count = following_count_element.text

    print(f"Followers: {followers_count}")
    print(f"Following: {following_count}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser after completion
    driver.quit()
