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
time.sleep(2)

# ===============================
# Wait & Click X Icon Dynamically
# ===============================
print("Waiting for X icon to appear (top-right clickable element)...")
time.sleep(2)
size = driver.get_window_size()
width = size['width']
height = size['height']

clicked = False
timeout = 10
interval = 0.5
elapsed = 0

while not clicked and elapsed < timeout:
    elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
    for el in elements:
        try:
            bounds = el.get_attribute("bounds")
            if bounds:
                x1y1, x2y2 = bounds.split('][')
                x1, y1 = map(int, x1y1.strip('[').split(','))
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
time.sleep(2)

# ===============================
# Click ALLOW ACCESS
# ===============================
print("Searching for 'Allow Access' button...")
allow_clicked = False
try:
    allow_btn = driver.find_element(
        AppiumBy.XPATH,
        "//*[contains(@text,'Allow') or contains(@text,'ALLOW') or contains(@text,'Allow Access')]"
    )
    allow_btn.click()
    allow_clicked = True
except NoSuchElementException:
    try:
        allow_btn = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Allow')]"
        )
        allow_btn.click()
        allow_clicked = True
    except NoSuchElementException:
        w, h = driver.get_window_size().values()
        driver.tap([(w//2, h//2)])
        allow_clicked = True

print("Allow Access clicked!" if allow_clicked else "Allow Access not found")
time.sleep(2)

# ===============================
# Click ALLOW Button Above "Don't Allow"
# ===============================
print("Clicking the correct 'Allow' button above 'Don't Allow'...")
allow_button_clicked = False
try:
    allow_btn = driver.find_element(
        AppiumBy.XPATH,
        "//android.widget.Button[@text='Allow']"
    )
    allow_btn.click()
    allow_button_clicked = True
except NoSuchElementException:
    print("Allow button not found")

print("Allow button clicked!" if allow_button_clicked else "Allow button not found")
time.sleep(2)

# ===============================
# Click Theme Change Icon (Moon)
# ===============================
print("Searching for Theme change (moon) icon...")
clicked = False
timeout = 10
interval = 0.5
elapsed = 0

size = driver.get_window_size()
width = size['width']
height = size['height']

while not clicked and elapsed < timeout:
    elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
    for el in elements:
        try:
            desc = el.get_attribute("content-desc")
            if desc and ("Theme" in desc or "Dark" in desc or "Night" in desc or "Moon" in desc):
                el.click()
                clicked = True
                print("Theme (moon) icon clicked via content-desc!")
                break
        except:
            continue
    if not clicked:
        driver.tap([(int(width*0.85), int(height*0.08))])
        clicked = True
        print("Theme (moon) icon clicked via coordinates fallback!")
        break
    time.sleep(interval)
    elapsed += interval

if not clicked:
    print("Theme (moon) icon not found!")
time.sleep(2)

# ===============================
# Click  Icon (after theme change)
# ===============================
print("Waiting for UI to stabilize after theme change...")
time.sleep(3)

settings_clicked = False
timeout = 15
interval = 0.5
elapsed = 0

size = driver.get_window_size()
width = size['width']
height = size['height']

while not settings_clicked and elapsed < timeout:
    try:
        elements = driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.ImageView[@clickable='true']"
        )
        for el in elements:
            bounds = el.get_attribute("bounds")
            if bounds:
                x1y1, x2y2 = bounds.split('][')
                x1, y1 = map(int, x1y1.strip('[').split(','))
                x2, y2 = map(int, x2y2.strip(']').split(','))
                if x1 > width * 0.6 and y1 < height * 0.2:
                    el.click()
                    settings_clicked = True
                    print("Language icon clicked successfully!")
                    break
        if not settings_clicked:
            driver.tap([(int(width*0.75), int(height*0.08))])
            settings_clicked = True
            print("Language icon clicked via fallback tap!")
    except:
        pass
    time.sleep(interval)
    elapsed += interval

if not settings_clicked:
    print("Language icon not found!")
    # ===============================
# Scroll & Select Urdu Language
# ===============================
print("Searching for Urdu language on Language screen...")
found = False
max_scrolls = 8

for _ in range(max_scrolls):
    try:
        # Try to find Urdu (in English or Urdu script)
        urdu = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@text,'Urdu') or contains(@text,'اردو')]"
        )
        urdu.click()
        print("Urdu language selected successfully!")
        found = True
        break
    except NoSuchElementException:
        # Swipe up to scroll
        driver.swipe(500, 1600, 500, 600, 800)
        time.sleep(1)

if not found:
    print("Urdu language not found. It may already be visible without scrolling.")
# ===============================
# Click Done button after selecting Urdu
# ===============================
print("Searching for Done button on Language screen...")

done_clicked = False
try:
    # Try text-based search
    done_btn = driver.find_element(
        AppiumBy.XPATH,
        "//*[@text='Done' or @text='DONE']"
    )
    done_btn.click()
    done_clicked = True
except NoSuchElementException:
    try:
        # Try content-desc search
        done_btn = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Done')]"
        )
        done_btn.click()
        done_clicked = True
    except NoSuchElementException:
        # Fallback tap on top-right corner
        size = driver.get_window_size()
        x = int(size['width'] * 0.95)
        y = int(size['height'] * 0.07)
        driver.tap([(x, y)])
        done_clicked = True

if done_clicked:
    print("Done button clicked successfully!")
else:
    print("Done button not found!")



