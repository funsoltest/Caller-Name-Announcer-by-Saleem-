from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
import time


class LanguagePage(BasePage):

    # -------- Locators --------
    ENGLISH_TEXT = (
        AppiumBy.XPATH,
        "//*[contains(@text,'English') or contains(@text,'ENGLISH')]"
    )

    DONE_BTN = (
        AppiumBy.XPATH,
        "//*[@text='Done' or @text='DONE']"
    )

    SKIP_BTN = (
        AppiumBy.XPATH,
        "//*[@text='Skip' or @text='SKIP']"
    )

    # -------- Actions --------
    def select_english(self):
        print("Selecting English language...")
        found = False

        for _ in range(8):
            try:
                self.wait_and_click(self.ENGLISH_TEXT, timeout=2)
                print("English selected")
                found = True
                break
            except TimeoutException:
                self.driver.swipe(500, 1600, 500, 600, 800)
                time.sleep(1)

        if not found:
            raise Exception("English language not found")

    def click_done(self):
        print("Clicking DONE button...")
        try:
            self.wait_and_click(self.DONE_BTN, timeout=5)
        except TimeoutException:
            size = self.driver.get_window_size()
            self.driver.tap([
                (int(size['width'] * 0.95), int(size['height'] * 0.07))
            ])
        time.sleep(1)

    def handle_onboarding_and_premium(self):
        print("Handling onboarding & premium screens...")

        # ---------- WAIT for Skip (up to 7 sec) ----------
        skip_clicked = False
        end_time = time.time() + 7

        while time.time() < end_time:
            try:
                self.driver.find_element(*self.SKIP_BTN).click()
                print("Skip clicked")
                skip_clicked = True
                break
            except NoSuchElementException:
                time.sleep(0.5)

        if not skip_clicked:
            print("Skip not found, continuing...")

        # ---------- WAIT for Premium X ----------
        print("Waiting for premium screen close...")
        time.sleep(5)  # IMPORTANT: premium animation delay

        size = self.driver.get_window_size()
        width, height = size['width'], size['height']

        clicked = False
        end_time = time.time() + 7

        while time.time() < end_time and not clicked:
            elements = self.driver.find_elements(
                AppiumBy.XPATH, "//*[@clickable='true']"
            )

            for el in elements:
                try:
                    bounds = el.get_attribute("bounds")
                    if bounds:
                        x1y1, _ = bounds.split('][')
                        x, y = map(int, x1y1.strip('[').split(','))

                        if x > width * 0.7 and y < height * 0.2:
                            el.click()
                            clicked = True
                            print("Premium close clicked")
                            break
                except:
                    continue

            time.sleep(0.5)

        if not clicked:
            print("Premium close not found, pressing BACK")
            self.driver.press_keycode(4)

        time.sleep(1)
