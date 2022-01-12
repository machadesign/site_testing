# methods need to be called from main method page
# need to specify the methods with their defined page locators for the page
from pages.base_page import BasePage
# also need to call By in order to specify locators
from selenium.webdriver.common.by import By


# access methods from the base_page BasePage class
class Homepage(BasePage):

    # - attributes of a DOM
    Element_ID = (By.ID, "front_image")
    Technologies_dropdown = (By.XPATH, '//*[@id="header"]/nav/ul/li[1]/div/a/strong[1]')
    Dropdown_element = (By.XPATH, '//*[@id="header"]/nav/ul/li[1]/div/div')
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
        self.driver.get("https://www.carnegietechnologies.com/")

    # check for the specific element on the page
    def check_hp_game_image(self):
        self.check_if_enabled(self.Element_ID)

    def hover_over_top_technologies(self):
        self.hover_over_element(self.Technologies_dropdown)

    # hp.return_css_property_value()

    def check_if_drop_active(self):
        # return_css_property_value
        value = self.return_css_property_value(by_locator=self.Dropdown_element, key="visibility")
        assert value == 'visible'

