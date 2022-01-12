# page contains the methods for the web pages
# the methods wait specified time until element is found
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
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

    # actions
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def send_keys_entry(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    # move mouse to middle of the element, use for elements w/ hover actions, positioning etc.
    # check content after hovering over element
    def hover_over_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        # performs all stored actions
        actions.perform()



    # check for elements
    # check and return element

    def check_if_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def check_for_return_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element

    def return_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title):
        element = WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return element.text


    # check if drop down menu is visible
    # - if so check if all links are shown
    # - create an array of expected links
    def return_css_property_value(self, by_locator, key):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        value = element.value_of_css_property(key)
        return value

# hover over element
# check new element within see if key: value is visible

# //*[@id="header"]/nav/ul/li[1]/div/a/strong[1]

# check id a list item exists in a list
# find

# <ul id="myId">
#     <li>Something here</li>
#     <li>And here</li>
#     <li>Even more here</li>
# </ul>
#
# html_list = self.driver.find_element_by_id("myId")
# items = html_list.find_elements_by_tag_name("li")
# for item in items:
#     text = item.text
#     print text

    # header nav ul li a:hover