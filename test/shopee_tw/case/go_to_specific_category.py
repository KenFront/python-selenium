import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test.browser_list import get_browser_list
from test.shopee_tw.pages import page_index
from test.shopee_tw.ui_components import css_selector
from test.shopee_tw.utils.clear_init_pop import clear_init_pop


def test_go_to_specific_category():
    for browser in get_browser_list():
        category_end = " | 蝦皮購物"
        browser.get(page_index)

        category_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector.CATEGORY_MAN_CLOTHING))
        )
        clear_init_pop(browser)

        category_link.click()
        time.sleep(1)
        assert category_end in browser.title
