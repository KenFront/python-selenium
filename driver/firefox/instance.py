from os import listdir
from re import match
from selenium import webdriver
from driver.utils.get_driver_path import get_driver_path


def run_firefox():
    return webdriver.Firefox(executable_path=get_driver_path('firefoxdriver'))


firefox = run_firefox()
