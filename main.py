import time
import logging

import pyautogui

from config import website_url, texts_to_check

from classes.ViewHandler import ViewHandler

logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

start_time = time.time()  # Record the start time


def log_run_start():
    logging.info(f"Starting a new run at {time.strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    vh = ViewHandler(website_url)
    log_run_start()

    # for text_to_check in texts_to_check:
    vh.take_screenshot_for_text(text_to_find='Zagraj teraz')
    vh.find_text_coordinates_on_screenshot(text_to_find='Zagraj teraz')
    time.sleep(20)

    # for text_to_check in texts_to_check:
    vh.take_screenshot_for_text(text_to_find='Zaloquisie')
    vh.find_text_coordinates_on_screenshot(text_to_find='Zaloquisie')
    time.sleep(5)

    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"Run completed in {duration:.2f} seconds")


if __name__ == "__main__":
    main()

