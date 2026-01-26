from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time

class DialerPage(BasePage):

    def open_dialer(self):
        self.wait_and_click((AppiumBy.XPATH, "//*[@text='Dialer']"))

    def dial_numbers(self, numbers):
        for num in numbers:
            self.wait_and_click((AppiumBy.XPATH, f"//*[@text='{num}']"))
            time.sleep(0.5)

    def press_call(self):
        size = self.driver.get_window_size()
        self.driver.tap([
            (size['width']//2, int(size['height']*0.85))
        ])
