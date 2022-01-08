# page contains the methods for the web pages
# the methods wait specified time until element is found
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html


# action occurs - expected condition specified
# until(method – callable(WebDriver) message – optional (message for TimeoutException))
# Page classes inherit the BasePage,


class BasePage:
    # pass the drive to this class to use it's methods
    # driver passed into Base page from parent
    def __init__(self, driver):
        self.driver = driver

    # check and return element
    def check_for_element_return_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element

    def check_for_element_if_exists(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

