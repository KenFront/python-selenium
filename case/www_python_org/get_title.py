def get_title(browser):
    try:
        assert 'Python' in browser.title
        print(browser.title)
        browser.quit()
    except AssertionError:
        print("AssertionError: {:s}".format(__name__))
        browser.quit()
