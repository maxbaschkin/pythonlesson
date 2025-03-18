import pytest
from selenium import webdriver
from pythonlesson.pages.homepage import HomePage

def test_webpage(browser):
    homepg = HomePage(browser)
    homepg.open()
