# methods need to be called from main method page
# need to specify the methods with their defined page locators for the page
from pages.base_page import BasePage
# also need to call By in order to specify locators
from selenium.webdriver.common.by import By


# access methods from the base_page BasePage class
class Homepage(BasePage):

    # - attributes of a DOM
    Element_ID = (By.ID, "front_image")
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name" , name = ""
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"

    def __init__(self, driver):
        super().__init__(driver)
        # call the variables from the parent class , the driver for getting page
        self.driver.get("http://www.wordrubblegame.com/")

    # check for the specific element on the page
    def check_hp_game_image(self):
        self.check_for_element_if_exists(self.Element_ID)



