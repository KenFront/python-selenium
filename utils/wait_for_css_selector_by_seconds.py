from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_for_css_selector_by_seconds(browser: WebDriver, css_selector, seconds):
    return WebDriverWait(browser, seconds).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, css_selector))
    )
