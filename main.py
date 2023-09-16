import time
import logging

import pyautogui

from config import website_url, login, password

from classes.ViewHandler import ViewHandler

logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

start_time = time.time()  # Record the start time


def log_run_start():
    logging.info(f"Starting a new run at {time.strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    vh = ViewHandler(website_url)
    log_run_start()

    time.sleep(3)
    vh.take_screenshot_for_id(screenshot_id='Zagraj teraz')
    vh.find_text_coordinates_on_screenshot(text_to_find='Zagraj teraz', screenshot_id='Zagraj teraz')
    time.sleep(6)

    vh.take_screenshot_for_id(screenshot_id='Zaloqujsie')
    vh.find_text_coordinates_on_screenshot(text_to_find='Zaloqujsie', screenshot_id='Zaloqujsie')
    time.sleep(5)

    vh.take_screenshot_for_id(screenshot_id='logowanie')
    vh.find_text_coordinates_on_screenshot(text_to_find='Billie Eillish', screenshot_id='logowanie')
    time.sleep(2)
    vh.type_text(text_to_type=login)
    time.sleep(2)
    vh.type_text(text_to_type=password)
    time.sleep(60)

    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"Run completed in {duration:.2f} seconds")


if __name__ == "__main__":
    main()

