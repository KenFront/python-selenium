import time
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.paths import report_path

def save_screenshot_by_timestamp(browser: WebDriver):
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    print("AssertionError: {:s}".format(__name__))
    browser.save_screenshot(
        '{:s}/{:s}_{:s}.png'.format(report_path, __name__, nowTime))
    browser.quit()
