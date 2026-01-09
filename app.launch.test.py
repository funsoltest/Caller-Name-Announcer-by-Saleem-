from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
# Appium server configuration
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
#paste app path 
options.app = r"C:\Users\saleem\Desktop\appium.test/CNA.apk"
# Connecting with appium server 
print("Connecting to Appium server...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("App launched successfully!")