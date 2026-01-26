from appium.options.android import UiAutomator2Options

def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app = r"C:\Users\saleem\Desktop\appium.test\CNA.apk"
    return options
