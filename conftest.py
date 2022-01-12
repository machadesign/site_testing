# conftest to provide fixtures to tests within it's own directory

# test against different browsers

# reference
# - https://www.selenium.dev/documentation/webdriver/capabilities/shared/

import pytest
from selenium import webdriver
# selenium package with the webdriver module, module with webdriver implementations
from selenium.webdriver.common.keys import Keys
# these keyboard keys to be used
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# https://www.selenium.dev/documentation/webdriver/capabilities/shared/

# CHROMEDRIVER_PATH
chrome_exe = '/Users/matthewchadwell/Desktop/webdrivers/chromedriver'
# ability to add options for the browser
# - options = webdriver.ChromeOptions()
service = ChromeService(executable_path=chrome_exe)


@pytest.fixture(scope="session")
# class multiple test cases will get called and drive ronly called once
# function , driver is called for each test case in a class
def return_driver(request):
    # create aof the chrome webdriver
    driver = webdriver.Chrome(service=service)
    # web_driver in request variable at a (scope=" ") level which can be accessed while running your test
    # request.cls.driver = driver
    # cleanup options -
    # option to just clear all cookies
    # web_driver.delete_all_cookies()
    # web_driver.get("chrome://settings/clearBrowserData")
    # - clear browsing history, cookies and cached images/files
    yield driver

    driver.close()

# specify window size 
