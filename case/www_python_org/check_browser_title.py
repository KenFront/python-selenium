from selenium.webdriver.chrome.webdriver import WebDriver
from case.www_python_org.pages import page_index
from utils.exceptions import save_screenshot_by_timestamp


def check_browser_title(browser: WebDriver):
    try:
        browser.get(page_index)
        assert 'Python' in browser.title
    except AssertionError:
        save_screenshot_by_timestamp(browser)
