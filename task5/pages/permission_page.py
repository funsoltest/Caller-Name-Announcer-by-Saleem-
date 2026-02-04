from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time


class PermissionPage(BasePage):

    # Original ID (app permission)
    APP_PERMISSION_BTN = (AppiumBy.ID, "calleridannounce.callernameannouncer.announcer.speaker:id/tvSaveChanges")
    # Additional ID (system permission)
    SYSTEM_PERMISSION_BTN = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")

    def handle_permissions(self):
        """Click the permission buttons sequentially"""
        print("Handling permissions...")

        # Click the app permission button first
        try:
            el1 = self.driver.find_element(*self.APP_PERMISSION_BTN)
            if el1.is_displayed():
                el1.click()
                print("App permission button clicked")
                time.sleep(1)
        except Exception:
            print("App permission button not found, moving on")

        # Then click the system permission button
        try:
            el2 = self.driver.find_element(*self.SYSTEM_PERMISSION_BTN)
            if el2.is_displayed():
                el2.click()
                print("System permission button clicked")
                time.sleep(1)
        except Exception:
            print("System permission button not found, moving on")
