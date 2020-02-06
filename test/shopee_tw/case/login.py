import time
import os
from selenium.webdriver.common.keys import Keys
from test.browser_list import get_browser_list
from test.shopee_tw.pages import page_index
from test.shopee_tw.ui_components import css_selector
from test.shopee_tw.utils.clear_init_pop import clear_init_pop
from utils.wait_for_css_selector_by_seconds import wait_for_css_selector_by_seconds


def login():
    for browser in get_browser_list():
        browser.get(page_index)
        login_btn = wait_for_css_selector_by_seconds(
            browser, css_selector.NAV_LOGIN_BTN, 10)
        clear_init_pop(browser)
        login_btn.click()
        login_pop_account_input = wait_for_css_selector_by_seconds(
            browser, css_selector.LOGIN_POP_ACCOUNT, 10)
        login_pop_password_input = browser.find_element_by_css_selector(
            css_selector.LOGIN_POP_PASSWORD)
        login_pop_account_input.send_keys(os.getenv('shopee_tw_account'))
        login_pop_password_input.send_keys(os.getenv('shopee_tw_password'))

        # need wait for input SMS code manually.

        nav_user_info = wait_for_css_selector_by_seconds(
            browser, css_selector.NAV_USER_INFO, 60)
        assert nav_user_info.text == os.getenv('shopee_tw_account')
