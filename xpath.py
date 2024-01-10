from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://www.instagram.com/guviofficial/"
driver.get(url)

try:
    # Task 1: Click on the first post (use XPath)
    first_post_xpath = "//article//a"
    first_post = driver.find_element(By.XPATH, first_post_xpath)
    first_post.click()

    # Wait for the post to load
    time.sleep(3)

    # Task 2: Like the post (use relative XPath)
    like_button_xpath = "//span[@aria-label='Like']"
    like_button = driver.find_element(By.XPATH, like_button_xpath)
    like_button.click()

    # Wait for a moment
    time.sleep(2)

    # Task 3: Comment on the post (use relative XPath)
    comment_input_xpath = "//textarea[@placeholder='Add a comment...']"
    comment_input = driver.find_element(By.XPATH, comment_input_xpath)
    comment_input.send_keys("This is an automated comment.")

    # Wait for a moment
    time.sleep(2)

    # Task 4: Post the comment (use relative XPath)
    post_comment_button_xpath = "//button[contains(text(), 'Post')]"
    post_comment_button = driver.find_element(By.XPATH, post_comment_button_xpath)
    post_comment_button.click()

    # Wait for a moment
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser after completion
    driver.quit()
