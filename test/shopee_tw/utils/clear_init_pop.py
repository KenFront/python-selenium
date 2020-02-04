from selenium.webdriver.chrome import webdriver
from test.shopee_tw.ui_components import css_selector


def clear_init_pop(browser: webdriver):
    pop_img_close_btn = browser.find_element_by_css_selector(
        css_selector.INIT_PAGE_POP_CLOSE_BTN)
    if pop_img_close_btn:
            pop_img_close_btn.click()
