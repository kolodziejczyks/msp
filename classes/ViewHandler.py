import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import easyocr
import numpy as np
import logging
from PIL import Image
import pyautogui


class ViewHandler:
    def __init__(self, website_url):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 768)
        self.website_url = website_url
        self.actions = ActionChains(self.driver)
        self.reader = easyocr.Reader(['pl'])

        # Load the website
        self.driver.get(self.website_url)
        self.canvas = self.driver.find_element('id', 'unity-canvas')

    def take_screenshot_for_text(self, text_to_find):
        screenshot_path = f'{text_to_find}.png'
        self.canvas.screenshot(screenshot_path)
        print(f'take screenshot for text {text_to_find}')

    def find_text_coordinates_on_screenshot(self, text_to_find):
        self.actions.move_by_offset(0, 0).click().perform()
        logging.info(f"Trying to find: {text_to_find}")

        screenshot_path = f'{text_to_find}.png'
        screenshot = Image.open(screenshot_path)
        image_np = np.array(screenshot)

        text = self.reader.readtext(image_np)
        print(text)

        found_texts = []
        found_text_coordinates = []

        # Check if any of the recognized text contains the specified texts
        for item in text:
            if text_to_find in item[1]:
                found_texts.append(text_to_find)
                found_text_coordinates.append(item[0])

        if found_texts:
            logging.info(f"The following texts were found: {', '.join(found_texts)}")
            logging.info(f"The coordinates of the found texts are: {found_text_coordinates}")

        if found_text_coordinates:
            first_text_coordinates = found_text_coordinates[0]
            text_x, text_y, text_w, text_h = first_text_coordinates[0][0], first_text_coordinates[0][1], \
                first_text_coordinates[2][0] - first_text_coordinates[0][0], first_text_coordinates[2][1] - \
                first_text_coordinates[0][1]
            center_x, center_y = int(text_x + text_w / 2), int(text_y + text_h / 2)
            logging.info(f"Clicking on the center of the text: {found_texts[0]}")
            logging.info(f"Coordinates of that click: {center_x}, {center_y}")
            self.actions.move_by_offset(center_x, center_y).click().perform()



