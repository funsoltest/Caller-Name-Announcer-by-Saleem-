from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PermissionPage(BasePage):

    # -------- Locators --------
    ALLOW_BTN = (AppiumBy.XPATH, "//*[contains(@text,'Allow')]")
    SYSTEM_ALLOW_BTN = (AppiumBy.XPATH, "//android.widget.Button[@text='Allow']")

    # -------- Actions --------
    def allow_access(self):
        if self.is_element_present(self.ALLOW_BTN, timeout=5):
            self.wait_and_click(self.ALLOW_BTN)
            print("App permission allow clicked")
            self.wait_for_element_not_present(self.ALLOW_BTN, timeout=8)

    def system_allow(self):
        if self.is_element_present(self.SYSTEM_ALLOW_BTN, timeout=5):
            self.wait_and_click(self.SYSTEM_ALLOW_BTN)
            print("System permission allow clicked")
            self.wait_for_element_not_present(self.SYSTEM_ALLOW_BTN, timeout=8)
