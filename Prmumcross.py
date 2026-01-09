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

time.sleep(2)

# ===============================
# Scroll & Select English
# ===============================
print("Searching for English language...")
found = False
for _ in range(8):
    try:
        driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@text,'English') or contains(@text,'ENGLISH')]"
        ).click()
        print("English language selected!")
        found = True
        break
    except NoSuchElementException:
        driver.swipe(500, 1600, 500, 600, 800)
        time.sleep(1)

if not found:
    print("English language not found.")

time.sleep(2)

# ===============================
# Click DONE
# ===============================
try:
    driver.find_element(AppiumBy.XPATH, "//*[@text='Done' or @text='DONE']").click()
except NoSuchElementException:
    # fallback tap top-right
    size = driver.get_window_size()
    driver.tap([(int(size['width']*0.95), int(size['height']*0.07))])
print("Done clicked")

time.sleep(2)

# ===============================
# Click SKIP
# ===============================
try:
    driver.find_element(AppiumBy.XPATH, "//*[@text='Skip' or @text='SKIP']").click()
except NoSuchElementException:
    driver.back()
print("Skip handled")

# ===============================
# Wait & Click X Icon Dynamically
# ===============================
print("Waiting for X icon to appear (top-right clickable element)...")
time.sleep(2)  # small initial delay for animation

size = driver.get_window_size()
width = size['width']
height = size['height']

clicked = False
timeout = 10  # maximum wait seconds
interval = 0.5
elapsed = 0

while not clicked and elapsed < timeout:
    # find all clickable elements
    elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
    for el in elements:
        try:
            bounds = el.get_attribute("bounds")  # format: [x1,y1][x2,y2]
            if bounds:
                x1y1, x2y2 = bounds.split('][')
                x1, y1 = map(int, x1y1.strip('[').split(','))
                x2, y2 = map(int, x2y2.strip(']').split(','))
                # check if element is in top-right area
                if x1 > width * 0.7 and y1 < height * 0.2:
                    el.click()
                    clicked = True
                    print("X icon clicked successfully!")
                    break
        except:
            continue
    if not clicked:
        time.sleep(interval)
        elapsed += interval

if not clicked:
    print("X icon not found, pressing BACK as fallback")
    driver.press_keycode(4)


