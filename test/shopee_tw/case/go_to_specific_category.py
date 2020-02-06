import time
from test.browser_list import get_browser_list
from test.shopee_tw.pages import page_index
from test.shopee_tw.ui_components import css_selector
from test.shopee_tw.utils.clear_init_pop import clear_init_pop
from utils.wait_for_css_selector_by_seconds import wait_for_css_selector_by_seconds


def test_go_to_specific_category():
    for browser in get_browser_list():
        category_end = " | 蝦皮購物"
        browser.get(page_index)

        category_link = wait_for_css_selector_by_seconds(
            browser, css_selector.CATEGORY_MAN_CLOTHING, 10)
        clear_init_pop(browser)

        category_link.click()
        time.sleep(1)
        assert category_end in browser.title
