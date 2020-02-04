from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test.browser_list import get_browser_list
from test.shopee_tw.pages import page_index
from test.shopee_tw.ui_components import css_selector
from test.shopee_tw.utils.clear_init_pop import clear_init_pop


def test_search_goods():
    for browser in get_browser_list():
        search_word = "筆電"
        browser.get(page_index)

        search_bar = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.SEARCH_BAR))
        )
        clear_init_pop(browser)
        search_bar.send_keys(search_word)
        search_bar.send_keys(Keys.ENTER)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.SEARCH_RESULT_LIST))
        )
        assert search_word in browser.title
