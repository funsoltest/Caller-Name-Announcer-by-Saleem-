from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

# ===============================
# Appium Configuration
# ===============================
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.app = r"C:\Users\saleem\Desktop\appium.test\CNA.apk"

# ===============================
# Start Appium Session
# ===============================
print("Connecting to Appium server...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("App launched successfully!")

time.sleep(3)

# ===============================
# Scroll Until English Found
# ===============================
print("Searching for English language...")

found = False
max_scrolls = 8

for _ in range(max_scrolls):
    try:
        english = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@text,'English') or contains(@text,'ENGLISH')]"
        )
        english.click()
        print("English language selected successfully!")
        found = True
        break
    except NoSuchElementException:
        # Swipe up to scroll
        driver.swipe(500, 1600, 500, 600, 800)
        time.sleep(1)

if not found:
    print("English language not found. Check text in UIAutomatorViewer.")

time.sleep(5)
driver.quit()
