# reference
# - https://www.selenium.dev/documentation/webdriver/capabilities/shared/

# these keyboard keys to be used
# https://www.selenium.dev/documentation/webdriver/capabilities/shared/

# from pages import Homepage
from pages.homepage import Homepage
# access methods w/ locators
# access webdriver

# capability to enter keys in tests

from pytest_bdd import scenario, then


# B_test = BasicTest()


# Scenarios

# - attributes of a DOM
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name" , name = ""
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"


# private methods for location elements
# (self,by,value)
# if specifed find_elements  , can return a list of elements within a class etc.


# If using classes with tests
#  - prefix your class with Test otherwise the class will be skipped

# test before adding request class to contain driver


# Pytest is trying run  tests from functions in Homepage as

# call driver from empty class
# class TestPage(BasicTest):
    # need to call an empty class w/ fixture , Pytest tries to run inherited class as a Testclass

    # use the request driver- create a class to get driver value , or specify the function name in conf

    # def test_check_for_element(self, return_driver):
    #     # gathers fixture data specified in contest file
    #     # fruits = driver.find_element(By.ID, "fruits")
    #     return_driver.get("http://www.wordrubblegame.com/")
    #     return_driver.find_element(By.ID, "front_image")

    # @scenario('../features/home_page.feature', 'Access homepage and view product image')


@scenario('/Users/matthewchadwell/PycharmProjects/examp_sel/tests/features/home_page.feature', 'Access homepage and view product image')
def test_hp():
    pass

# any “@given” step function that returns a value can also be used as a fixture

# @then('The game image should be shown')
# def test_check_for_image(return_driver):
#     # call methods w/ locators from the page
#     # call driver from BasicTest class fixture
#     hp = Homepage(return_driver)
#     hp.check_hp_game_image()

@then('Hover over nav bar technology item')
def test_hover(return_driver):
    hp = Homepage(return_driver)
    hp.hover_over_top_technologies()
    hp.check_if_drop_active()

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4




# @scenario('/Users/matthewchadwell/PycharmProjects/examp_sel/tests/features/home_page.feature', 'Access homepage and view product image')
# def test_hp(self):
#     pass
#
# # any “@given” step function that returns a value can also be used as a fixture
#
# @then('Then The game image should be shown')
# def test_check_for_image(self):
#     # call methods w/ locators from the page
#     # call driver from BasicTest class fixture
#     self.hp = Homepage(self.driver)
#     self.hp.check_hp_game_image()
#
# def func(self, x):
#     return x + 1
#
# def test_answer(self):
#     assert self.func(3) == 4

