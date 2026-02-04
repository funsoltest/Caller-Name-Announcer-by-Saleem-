from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
import time


class LanguagePage(BasePage):

    ENGLISH_TEXT = (
        AppiumBy.XPATH,
        "//*[contains(@text,'English') or contains(@text,'ENGLISH')]"
    )

    DONE_BTN = (
        AppiumBy.ID,
        "calleridannounce.callernameannouncer.announcer.speaker:id/tvDone"
    )

    SKIP_BTN = (
        AppiumBy.XPATH,
        "//*[@text='Skip' or @text='SKIP']"
    )

    PREMIUM_CROSS_BTN = (
        AppiumBy.ACCESSIBILITY_ID,  # Using your recorded Accessibility ID
        "Image here"
    )

    def complete_language_flow(self):
        # Step 1: Wait for splash/language screen
        self.wait_for_language_page()

        # Step 2: Verify English is visible
        self.verify_english_present()

        # Step 3: Click DONE
        self.click_done_hard()

        # Step 4: Handle onboarding/premium screens
        self.handle_onboarding_and_premium()

        # Step 5: Handle premium cross button reliably
        self.handle_premium_cross()

    def wait_for_language_page(self, timeout=10):
        """Wait until the language selection screen is visible"""
        print("Waiting for language screen to appear...")
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                el = self.driver.find_element(*self.ENGLISH_TEXT)
                if el.is_displayed():
                    print("Language screen is visible")
                    return
            except NoSuchElementException:
                time.sleep(0.5)
        raise Exception("Language screen did not appear after splash")

    def verify_english_present(self):
        """Check that English option is present; no need to click if auto-selected"""
        print("Verifying English language presence...")
        try:
            el = self.wait_for_element(self.ENGLISH_TEXT, timeout=5)
            if el.is_displayed():
                print("English option is visible (assumed auto-selected)")
            else:
                raise Exception("English option is not visible")
        except TimeoutException:
            raise Exception("English option not found on language screen")

    def click_done_hard(self):
        """Click DONE button using ID with fallback tap"""
        print("Clicking DONE button (ID first, fallback tap)...")

        size = self.driver.get_window_size()
        tap_x = int(size['width'] * 0.95)
        tap_y = int(size['height'] * 0.07)

        try:
            done_btn = self.wait_for_element(self.DONE_BTN, timeout=3)
            done_btn.click()
            print("DONE button clicked via ID")
        except TimeoutException:
            print("DONE button not found via ID, performing tap fallback")
            self.driver.tap([(tap_x, tap_y)])
        
        time.sleep(2)

    def handle_onboarding_and_premium(self):
        """Handle Skip/onboarding screens"""
        print("Handling onboarding & premium screens...")

        end_time = time.time() + 8
        while time.time() < end_time:
            try:
                self.driver.find_element(*self.SKIP_BTN).click()
                print("Skip clicked")
                return
            except NoSuchElementException:
                time.sleep(0.5)

        # fallback
        print("Skip not shown, pressing BACK")
        self.driver.press_keycode(4)

    def handle_premium_cross(self, timeout=8):
        """Wait 5 seconds for premium cross button to appear and click it"""
        print("Waiting 5 seconds for premium screen cross button...")
        time.sleep(5)

        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                cross_btn = self.driver.find_element(*self.PREMIUM_CROSS_BTN)
                if cross_btn.is_displayed():
                    cross_btn.click()
                    print("Premium cross button clicked")
                    return
            except NoSuchElementException:
                time.sleep(0.5)

        print("Premium cross button not shown, continuing")
