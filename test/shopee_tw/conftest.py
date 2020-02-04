from test.shopee_tw.case.login import login


def pytest_runtestloop():
    login()
