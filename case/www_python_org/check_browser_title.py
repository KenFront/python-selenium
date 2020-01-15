import time
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.paths import report_path
from case.www_python_org.pages import page_index


def check_browser_title(browser: WebDriver):
    try:
        browser.get(page_index)
        assert 'Python' in browser.title
    except AssertionError:
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        print("AssertionError: {:s}".format(__name__))
        browser.save_screenshot(
            '{:s}/{:s}_{:s}.png'.format(report_path, __name__, nowTime))
        browser.quit()
