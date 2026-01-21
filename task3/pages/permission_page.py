from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class PermissionPage:

    def __init__(self, driver):
        self.driver = driver

    def allow_access(self):
        try:
            self.driver.find_element(
                AppiumBy.XPATH,
                "//*[contains(@text,'Allow')]"
            ).click()
        except NoSuchElementException:
            self.driver.back()

    def system_allow(self):
        try:
            self.driver.find_element(
                AppiumBy.XPATH,
                "//android.widget.Button[@text='Allow']"
            ).click()
        except NoSuchElementException:
            pass
