from driver.firefox.instance import run_firefox
from driver.chrome.instance import run_chrome
from selenium.webdriver.chrome import webdriver

browser_list = [run_chrome(), run_firefox()]


def get_browser_list() -> [webdriver]:
    return browser_list
