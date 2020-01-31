from selenium.webdriver.chrome.webdriver import WebDriver
from case.www_python_org.pages import page_index
from case.browser_list import browser_list


def test_check_browser_title():
    for browser in browser_list:
        browser.get(page_index)
        assert 'Python' in browser.title
