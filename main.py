import time
import logging

import pyautogui

from config import website_url, login, password, destinationLogin

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
    time.sleep(3)

    vh.take_screenshot_for_id(screenshot_id='Zaloqujsie')
    vh.find_text_coordinates_on_screenshot(text_to_find='Zaloqujsie', screenshot_id='Zaloqujsie')
    # time.sleep(3)

    # pierwszy wynik na liscie zalogowanych
    vh.click_on_coordinates(504, 295)
    time.sleep(2)
    vh.type_text(text_to_type=login)
    time.sleep(2)
    vh.type_text(text_to_type=password)
    time.sleep(22)

    # przeklikanie sie przez intro
    # vh.neutral_click()
    # vh.neutral_click()
    # vh.neutral_click()
    # time.sleep(5)
    # vh.neutral_click()
    # vh.neutral_click()
    # vh.neutral_click()
    # time.sleep(5)

    # wyszukanie i danie grafa
    # profil
    vh.click_on_coordinates(40, 40)
    # friends
    vh.click_on_coordinates(610, 290)
    # time.sleep(5)
    vh.single_click_on_coordinates(0, 0)
    # vh.single_click_on_coordinates(968, 176)
    # to pierwsze we friends popup
    time.sleep(1)
    vh.click_on_coordinates(790, 178)
    # lupka
    time.sleep(1)
    vh.click_on_coordinates(893, 178)
    # search input
    time.sleep(2)
    vh.click_on_coordinates(836, 226)
    vh.type_text(text_to_type=destinationLogin)
    time.sleep(3)
    # pierwszy wynik na liście
    vh.click_on_coordinates(723, 300)
    time.sleep(3)
    # danie grafa
    vh.click_on_coordinates(617, 404)

    time.sleep(30)

    end_time = time.time()
    duration = end_time - start_time
    vh.take_screenshot_for_id(screenshot_id='finish')
    logging.info(f"Run completed in {duration:.2f} seconds")


if __name__ == "__main__":
    main()

