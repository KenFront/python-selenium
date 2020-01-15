from os import listdir
from re import match
from selenium import webdriver
from driver.utils.get_driver_path import get_driver_path

def run_chrome():
    return webdriver.Chrome(get_driver_path('chromedriver'))