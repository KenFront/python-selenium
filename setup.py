from selenium import webdriver
from case.get_title import get_title

chrome = webdriver.Chrome('./chromedriver.79')

get_title(chrome)
