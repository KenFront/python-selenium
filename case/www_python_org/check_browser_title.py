import time
from constants.paths import report_path

def check_browser_title(browser):
    try:
        browser.get('https://www.python.org/')
        assert 'Python' in browser.title
    except AssertionError:
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        print("AssertionError: {:s}".format(__name__))
        browser.save_screenshot(
            '{:s}/{:s}_{:s}.png'.format(report_path, __name__, nowTime))
        browser.quit()
