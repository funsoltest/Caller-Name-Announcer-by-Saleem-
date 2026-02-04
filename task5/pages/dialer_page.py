from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class DialerPage(BasePage):

    DIALER = (AppiumBy.XPATH, "//*[@text='Dialer']")  # update if needed

    def open_dialer(self):
        print("Opening dialer...")
        retries = 5
        for attempt in range(retries):
            try:
                self.wait_and_click(self.DIALER, timeout=5)
                print("Dialer opened successfully")
                return
            except Exception as e:
                print(f"Attempt {attempt+1}: Dialer not found yet, retrying...")
                time.sleep(1)
        raise Exception("Failed to open dialer: element not found")
