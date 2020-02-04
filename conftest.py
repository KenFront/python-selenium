from dotenv import load_dotenv
from test.browser_list import get_browser_list


def pytest_sessionstart():
    load_dotenv(dotenv_path='.env')


def pytest_sessionfinish():
    for browser in get_browser_list():
        browser.quit()
