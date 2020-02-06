from selenium.webdriver.common.keys import Keys
from test.browser_list import get_browser_list
from test.shopee_tw.pages import page_index
from test.shopee_tw.ui_components import css_selector
from test.shopee_tw.utils.clear_init_pop import clear_init_pop
from utils.wait_for_css_selector_by_seconds import wait_for_css_selector_by_seconds


def test_search_goods():
    for browser in get_browser_list():
        search_word = "筆電"
        browser.get(page_index)

        search_bar = wait_for_css_selector_by_seconds(
            browser, css_selector.SEARCH_BAR, 10)
        clear_init_pop(browser)
        search_bar.send_keys(search_word)
        search_bar.send_keys(Keys.ENTER)
        wait_for_css_selector_by_seconds(
            browser, css_selector.SEARCH_RESULT_LIST, 10)
        assert search_word in browser.title
