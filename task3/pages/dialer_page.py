from appium.webdriver.common.appiumby import AppiumBy
import time

class DialerPage:

    def __init__(self, driver):
        self.driver = driver

    def open_dialer(self):
        self.driver.find_element(
            AppiumBy.XPATH,"//*[@text='Dialer']"
        ).click()

    def dial_numbers(self, numbers):
        for num in numbers:
            self.driver.find_element(
                AppiumBy.XPATH, f"//*[@text='{num}']"
            ).click()
            time.sleep(0.5)

    def press_call(self):
        size = self.driver.get_window_size()
        self.driver.tap([
            (size['width']//2, int(size['height']*0.85))
        ])
