import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test.browser_list import get_browser_list
from test.shopee_tw.pages import page_index
from test.shopee_tw.ui_components import css_selector
from test.shopee_tw.utils.clear_init_pop import clear_init_pop


def login():
    for browser in get_browser_list():
        browser.get(page_index)
        login_btn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.NAV_LOGIN_BTN))
        )
        clear_init_pop(browser)
        login_btn.click()
        login_pop_account_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.LOGIN_POP_ACCOUNT))
        )
        login_pop_password_input = browser.find_element_by_css_selector(
            css_selector.LOGIN_POP_PASSWORD)
        login_pop_account_input.send_keys(os.getenv('shopee_tw_account'))
        login_pop_password_input.send_keys(os.getenv('shopee_tw_password'))

        # need wait for input SMS code manually.

        nav_user_info = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.NAV_USER_INFO))
        )
        assert nav_user_info.text == os.getenv('shopee_tw_account')
