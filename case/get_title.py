def get_title(browser):
    browser.get('https://www.python.org/')
    assert 'Python' in browser.title

    print(browser.title)

    browser.quit()
