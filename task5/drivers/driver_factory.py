from appium import webdriver
from config.capabilities import get_android_options

def create_driver():
    return webdriver.Remote(
        "http://127.0.0.1:4723",
        options=get_android_options()
    )
