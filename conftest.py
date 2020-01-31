from driver.chrome.instance import run_chrome
from driver.firefox.instance import run_firefox
from case.browser_list import browser_list


def pytest_sessionstart():
    browser_list.append(run_chrome())
    browser_list.append(run_firefox())


def pytest_sessionfinish():
    for browser in browser_list:
        browser.quit()
