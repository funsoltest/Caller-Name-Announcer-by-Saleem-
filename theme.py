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
time.sleep(2)  # initial delay for animation

size = driver.get_window_size()
width = size['width']
height = size['height']

clicked = False
timeout = 10  # maximum wait seconds
interval = 0.5
elapsed = 0

while not clicked and elapsed < timeout:
    elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
    for el in elements:
        try:
            bounds = el.get_attribute("bounds")  # format: [x1,y1][x2,y2]
            if bounds:
                x1y1, x2y2 = bounds.split('][')
                x1, y1 = map(int, x1y1.strip('[').split(','))
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
    # Only select the top button with text 'Allow'
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
        # fallback: tap top-right region
        driver.tap([(int(width*0.85), int(height*0.08))])
        clicked = True
        print("Theme icon clicked via coordinates fallback!")
        break
    time.sleep(interval)
    elapsed += interval

if not clicked:
    print("Theme  icon not found!")
# ===============================
# Click Dialer Icon at Bottom by Text
# ===============================
print("Waiting for 3 seconds before clicking Dialer icon...")
time.sleep(3)  # allow UI to settle

clicked = False
try:
    # Find the element which has text 'Dialer'
    dialer_icon = driver.find_element(
        AppiumBy.XPATH,
        "//*[@text='Dialer']"
    )
    dialer_icon.click()
    clicked = True
    print("Dialer icon clicked successfully!")
except NoSuchElementException:
    print("Dialer icon with text 'Dialer' not found!")
# ===============================
# Click Random Numbers on Dialer
# ===============================
import random

numbers_to_press = ['0', '1', '2', '3']  # the numbers you want to click
print("Clicking random numbers on Dialer:", numbers_to_press)

for num in numbers_to_press:
    try:
        btn = driver.find_element(AppiumBy.XPATH, f"//*[@text='{num}']")
        btn.click()
        print(f"Clicked number: {num}")
        time.sleep(0.5)  # small delay between clicks
    except NoSuchElementException:
        print(f"Number {num} button not found!")
# ===============================
# Click Phone Icon (Green Call Button)
# ===============================
print("Clicking Phone icon (green button below 0)...")
time.sleep(1)  # slight delay before clicking

# Get screen size
size = driver.get_window_size()
width = size['width']
height = size['height']

# Approximate position of the phone icon:
# Dial pad usually has 0 at bottom-center, phone icon just below it
x = width // 2
y = int(height * 0.85)  # slightly above bottom, adjust if needed

try:
    driver.tap([(x, y)])
    print("Phone icon clicked successfully!")
except:
    print("Failed to click Phone icon!")
# ===============================
# Select Caller Name Announcer & Set as Default
# ===============================
print("Waiting for Caller Name Announcer dialog to appear...")
time.sleep(2)  # wait for the dialog to appear

# Click "Caller Name Announcer"
try:
    caller_option = driver.find_element(
        AppiumBy.XPATH,
        "//*[@text='Caller Name Announcer']"
    )
    caller_option.click()
    print("Caller Name Announcer option clicked successfully!")
except NoSuchElementException:
    print("Caller Name Announcer option not found!")

time.sleep(1)  # short delay

# Click "Set as default" button
try:
    set_default_btn = driver.find_element(
        AppiumBy.XPATH,
        "//*[@text='Set as default']"
    )
    set_default_btn.click()
    print("Set as default clicked successfully!")
except NoSuchElementException:
    print("Set as default button not found!")





