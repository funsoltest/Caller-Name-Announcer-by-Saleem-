from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    # ---------- WAIT FOR ELEMENT ----------
    def wait_for_element(self, locator, timeout=None):
        return WebDriverWait(
            self.driver, timeout or self.DEFAULT_TIMEOUT
        ).until(EC.presence_of_element_located(locator))

    # ---------- WAIT & CLICK ----------
    def wait_and_click(self, locator, timeout=None):
        element = WebDriverWait(
            self.driver, timeout or self.DEFAULT_TIMEOUT
        ).until(EC.element_to_be_clickable(locator))
        element.click()

    # ---------- SEND KEYS ----------
    def wait_and_send_keys(self, locator, text, timeout=None):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # ---------- CHECK PRESENCE ----------
    def is_element_present(self, locator, timeout=5):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    # ---------- WAIT UNTIL DISAPPEAR ----------
    def wait_for_element_not_present(self, locator, timeout=None):
        WebDriverWait(
            self.driver, timeout or self.DEFAULT_TIMEOUT
        ).until_not(EC.presence_of_element_located(locator))

    # ---------- SAFE CLICK ----------
    def safe_click(self, locator, timeout=3):
        if self.is_element_present(locator, timeout):
            self.wait_and_click(locator, timeout)
