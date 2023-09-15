import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import easyocr
import numpy as np
import logging

# Configure logging
logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to log a message with a timestamp
def log_run_start():
    logging.info(f"Starting a new run at {time.strftime('%Y-%m-%d %H:%M:%S')}")


# Set up the WebDriver (assuming Chrome WebDriver)
driver = webdriver.Chrome()

# Define the login page URL without "/login"
login_url = 'https://www.moviestarplanet2.com'  # Updated URL to www.moviestarplanet2.com

# Provide the login and password
login = 'Billie Eillish - fake'  # Updated login
password = 'abcd1234'  # Updated password

# Set up the WebDriverWait with a timeout of 8 seconds
wait = WebDriverWait(driver, 8)  # Adjust the timeout as needed

# Texts to check for
texts_to_check = ['Zagraj teraz', 'Zaloguj się']  # Updated texts to check

# Loop through the accounts and automate login
driver.get(login_url)

# Log the start of the run
log_run_start()

# Initialize the start_time variable
start_time = time.time()

# Wait for the canvas to load (using the updated canvas ID)
canvas_location = wait.until(EC.presence_of_element_located((By.ID, 'unity-canvas')))  # Updated canvas ID

# Scroll to the canvas element to ensure it's within the viewport
driver.execute_script("arguments[0].scrollIntoView();", canvas_location)

# Capture a screenshot of the canvas using pyautogui
canvas_screenshot = pyautogui.screenshot()
canvas_screenshot.save('canvas_screenshot.png')

# Use easyocr to extract text from the screenshot with Polish language setting
reader = easyocr.Reader(['pl'])  # Change 'en' to 'pl' for Polish language
image_np = np.array(canvas_screenshot)  # Convert the screenshot to a NumPy array
text = reader.readtext(image_np)  # Use the NumPy array as input

# Initialize found_texts as an empty list
found_texts = []

# Initialize found_text_coordinates as an empty list
found_text_coordinates = []

# Check if any of the recognized text contains the specified texts
for item in text:
    for text_to_check in texts_to_check:
        if text_to_check in item[1]:
            found_texts.append(text_to_check)
            found_text_coordinates.append(item[0])

# Check if any of the specified texts were found
if found_texts:
    logging.info(f"The following texts were found: {', '.join(found_texts)}")

    # Sleep for a few seconds before clicking the first text (maximum 5 seconds)
    sleep_duration = min(5, 5 - (time.time() - start_time))  # Adjust the maximum wait time
    if sleep_duration > 0:
        time.sleep(sleep_duration)

    # Click on the center of the first found text
    if found_text_coordinates:
        first_text_coordinates = found_text_coordinates[0]
        text_x, text_y, text_w, text_h = first_text_coordinates[0][0], first_text_coordinates[0][1], \
        first_text_coordinates[2][0] - first_text_coordinates[0][0], first_text_coordinates[2][1] - \
        first_text_coordinates[0][1]
        center_x, center_y = int(text_x + text_w / 2), int(text_y + text_h / 2)  # Convert to integers

        # Record the time before clicking the first text
        click_time1 = time.time()

        # Click on the center of the text using its calculated coordinates
        pyautogui.click(center_x, center_y)

        # Record the time after clicking the first text
        click_time2 = time.time()

        logging.info(f"Clicked on the center of the first found text: {found_texts[0]}")
        logging.info(f"Time taken to click the first text: {click_time2 - click_time1:.2f} seconds")

        # Sleep for an additional 5 seconds before clicking the second text
        time.sleep(30)  # Adjust the duration as needed

    # Check if there are at least two elements in found_text_coordinates before clicking the second text
    if len(found_text_coordinates) >= 2:
        # Sleep for a few seconds before clicking the second text (maximum 5 seconds)
        sleep_duration = min(5, 5 - (time.time() - start_time))  # Adjust the maximum wait time
        if sleep_duration > 0:
            time.sleep(sleep_duration)

        # Find the coordinates of the second text and click on it
        second_text_coordinates = found_text_coordinates[1]
        second_text_x, second_text_y, second_text_w, second_text_h = second_text_coordinates[0][0], \
        second_text_coordinates[0][1], second_text_coordinates[2][0] - second_text_coordinates[0][0], \
                                       second_text_coordinates[2][1] - second_text_coordinates[0][1]
        second_center_x, second_center_y = int(second_text_x + second_text_w / 2), int(
            second_text_y + second_text_h / 2)  # Convert to integers

        # Record the time before clicking the second text
        click_time3 = time.time()

        # Click on the center of the second found text
        pyautogui.click(second_center_x, second_center_y)

        # Record the time after clicking the second text
        click_time4 = time.time()

        logging.info(f"Clicked on the center of the second found text: {found_texts[1]}")
        logging.info(f"Time taken to click the second text: {click_time4 - click_time3:.2f} seconds")

# Calculate the duration of the run and log it
end_time = time.time()
duration = end_time - start_time
logging.info(f"Run completed in {duration:.2f} seconds")

# The browser will stay open after clicking on the second text
