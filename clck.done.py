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
        driver.swipe(500, 1600, 500, 600, 800)
        time.sleep(1)

if not found:
    print("English language not found.")

time.sleep(2)

# ===============================
# Find & Click DONE Button
# ===============================
print("Searching for Done button...")
done_clicked = False

try:
    done_btn = driver.find_element(
        AppiumBy.XPATH,
        "//*[@text='Done' or @text='DONE']"
    )
    done_btn.click()
    done_clicked = True

except NoSuchElementException:
    try:
        done_btn = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Done')]"
        )
        done_btn.click()
        done_clicked = True

    except NoSuchElementException:
        size = driver.get_window_size()
        driver.tap([(size['width'] - 50, 80)])
        done_clicked = True

if done_clicked:
    print("Done button clicked successfully!")
else:
    print("Done button not found.")

time.sleep(2)

# ===============================
# Find & Click SKIP Button
# ===============================
print("Searching for Skip button...")
skip_clicked = False

try:
    skip_btn = driver.find_element(
        AppiumBy.XPATH,
        "//*[@text='Skip' or @text='SKIP']"
    )
    skip_btn.click()
    skip_clicked = True

except NoSuchElementException:
    try:
        skip_btn = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Skip')]"
        )
        skip_btn.click()
        skip_clicked = True

    except NoSuchElementException:
        try:
            skip_btn = driver.find_element(
                AppiumBy.XPATH,
                "//*[contains(@text,'Skip')]"
            )
            skip_btn.click()
            skip_clicked = True

        except NoSuchElementException:
            size = driver.get_window_size()
            driver.tap([(size['width'] - 50, 80)])
            skip_clicked = True

if skip_clicked:
    print("Skip button clicked successfully!")
else:
    print("Skip button not found.")


