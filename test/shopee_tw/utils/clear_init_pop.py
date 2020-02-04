from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from test.shopee_tw.ui_components import css_selector


def is_init_pop_exist(browser: webdriver):
    try:
        return WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.INIT_PAGE_POP_CLOSE_BTN))
        )
    except TimeoutException:
        return False


def clear_init_pop(browser: webdriver):
    pop_img_close_btn = is_init_pop_exist(browser)
    if pop_img_close_btn:
        pop_img_close_btn.click()
