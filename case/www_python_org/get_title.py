def get_title(browser):
    try:
        browser.get('https://www.python.org/')
        assert 'Python' in browser.title
        print(browser.title)
    except AssertionError:
        print("AssertionError: {:s}".format(__name__))
        browser.quit()
