from os import listdir
from re import match
from selenium import webdriver
from case.www_python_org.get_title import get_title


def find_chrome_driver_by_file_name(variable):
    return match('chromedriver', variable)


def get_chrome_driver_path():
    root_path = "./"
    root_foler_list = listdir(root_path)
    chrome_driver_path = list(
        filter(find_chrome_driver_by_file_name, root_foler_list))
    if len(chrome_driver_path) == 1:
        return root_path + chrome_driver_path[0]
    elif len(chrome_driver_path) == 0:
        raise ValueError('There is no chrome driver in project root path.')
    else:
        raise ValueError('There are more than one chrome driver in project root path.')


chrome = webdriver.Chrome(get_chrome_driver_path())
