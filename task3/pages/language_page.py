from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
import random

class LanguagePage:
    def __init__(self, driver):
        self.driver = driver

    def select_english(self):
        print("Selecting English language...")
        found = False
        for _ in range(8):
            try:
                self.driver.find_element(
                    AppiumBy.XPATH,
                    "//*[contains(@text,'English') or contains(@text,'ENGLISH')]"
                ).click()
                print("English selected")
                found = True
                break
            except NoSuchElementException:
                self.driver.swipe(500, 1600, 500, 600, 800)
                time.sleep(1)
        if not found:
            print("English not found")

    def click_done(self):
        print("Clicking DONE button...")
        try:
            self.driver.find_element(AppiumBy.XPATH, "//*[@text='Done' or @text='DONE']").click()
        except NoSuchElementException:
            size = self.driver.get_window_size()
            self.driver.tap([(int(size['width']*0.95), int(size['height']*0.07))])
        time.sleep(1)

    def click_skip_and_handle_premium(self):
        print("Handling Skip & Premium screens...")

        # ---------------- Skip Button ----------------
        try:
            skip_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Skip' or @text='SKIP']")
            skip_btn.click()
            print("Skip clicked successfully!")
        except NoSuchElementException:
            print("Skip not found, continuing...")

        time.sleep(random.uniform(1.5, 2.5))

        # ---------------- Premium X Button ----------------
        size = self.driver.get_window_size()
        width, height = size['width'], size['height']

        clicked = False
        timeout = 10  # wait max 10 sec
        interval = 0.5
        elapsed = 0

        while not clicked and elapsed < timeout:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
            for el in elements:
                try:
                    bounds = el.get_attribute("bounds")  # [x1,y1][x2,y2]
                    if bounds:
                        x1y1, x2y2 = bounds.split('][')
                        x1, y1 = map(int, x1y1.strip('[').split(','))
                        # check if element in top-right area
                        if x1 > width * 0.7 and y1 < height * 0.2:
                            el.click()
                            clicked = True
                            print("Premium X icon clicked successfully!")
                            break
                except:
                    continue
            if not clicked:
                time.sleep(interval)
                elapsed += interval

        if not clicked:
            print("Premium X icon not found, pressing BACK as fallback")
            self.driver.press_keycode(4)

        time.sleep(5)
