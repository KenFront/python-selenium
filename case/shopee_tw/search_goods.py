from case.shopee_tw.pages import page_index
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from case.browser_list import browser_list


def test_search_goods():
    for browser in browser_list:
        search_word = "筆電"
        browser.get(page_index)

        search_bar = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".shopee-searchbar .shopee-searchbar-input__input"))
        )
        search_bar.send_keys(search_word)
        search_bar.send_keys(Keys.ENTER)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".container > div[role='main']"))
        )
        assert search_word in browser.title
