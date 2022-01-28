# methods need to be called from main method page
# need to specify the methods with their defined page locators for the page
from pages.base_page import BasePage
# also need to call By in order to specify locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# access methods from the base_page BasePage class
class Homepage(BasePage):

    Carnegie_logo = (By.ID, "logo")
    Mission_statement = (By.ID, "hero-heading")


    Technologies_dropdown = (By.XPATH, '//*[@id="header"]/nav/ul/li[1]/div/a/strong[1]')
    # check Technology section drop down  visibility value, drop down shown
    Technology_dropdown_element = (By.XPATH, '//*[@id="header"]/nav/ul/li[1]/div/div')

    Company_dropdown = (By.XPATH, '//*[@id="header"]/nav/ul/li[2]/div/a/strong[1]')
    # check Company section drop down  visibility value, drop down shown
    Company_dropdown_element = (By.XPATH, '//*[@id="header"]/nav/ul/li[2]/div/div')

    # NAVBAR - TECHNOLOGIES- DROPDOWN OPTIONS
    # header/nav bar check, specify each so that can be called for BDD
    Nav_bar_Fintech_link_text = (By.LINK_TEXT, "FINTECH")
    Nav_bar_Valorus_link_text = (By.LINK_TEXT, "Valorus")
    Nav_bar_Satellite_link_text = (By.LINK_TEXT, "SATELLITE")
    Nav_bar_Carnegie_Satellite_link_text = (By.LINK_TEXT, "Carnegie Satellite Solutions")

    Nav_bar_MOBILITY_link_text = (By.LINK_TEXT, "MOBILITY")
    Nav_bar_NCP_link_text = (By.LINK_TEXT, "NCP")
    Nav_bar_Longview_link_text = (By.LINK_TEXT, "Longview")
    # <small> tag, not an anchor (<a>) link. XPath specified
    # - there are two links with same link text in - header/nav and footer
    Nav_bar_SaaS_link_text = (By.XPATH, '//*[@id="header"]/nav/ul/li[1]/div/div/div/p[5]/a[1]/small')
    Nav_bar_Octupus_link_text = (By.LINK_TEXT, "Octopus Space")

    # NAVBAR - COMPANY - DROPDOWN OPTIONS
    # header/nav bar check, specify each so that can be called for BDD
    Nav_bar_History_link_text = (By.LINK_TEXT, "History")
    Nav_bar_Focus_link_text = (By.LINK_TEXT, "Focus")
    Nav_bar_Vision_link_text = (By.LINK_TEXT, "Vision")
    Nav_bar_Values_link_text = (By.LINK_TEXT, "Values")

    # <strong> tag , not anchor (<a>) link, XPath specified
    Nav_bar_Contact = (By.XPATH, '//*[@id="header"]/nav/ul/li[3]/a/strong')


    # list to iterate check homepage for all items shown for links
    Technology_Nav_list = [Nav_bar_Fintech_link_text, Nav_bar_Valorus_link_text, Nav_bar_Carnegie_Satellite_link_text,
                           Nav_bar_Carnegie_Satellite_link_text, Nav_bar_MOBILITY_link_text, Nav_bar_NCP_link_text,
                           Nav_bar_Longview_link_text, Nav_bar_SaaS_link_text, Nav_bar_Octupus_link_text,
                           Nav_bar_Octupus_link_text]

    Company_Nav_list = [Nav_bar_History_link_text,Nav_bar_Focus_link_text,Nav_bar_Vision_link_text,
                        Nav_bar_Values_link_text]

    def __init__(self, driver):
        super().__init__(driver)
        # call the variables from the parent class , the driver for getting page
        self.driver.get("https://www.carnegietechnologies.com/")

    # check for the specific element on the page
    def check_hp_game_image(self):
        self.check_if_enabled(self.Carnegie_logo)

    def check_mission_statement(self):
        self.check_if_enabled(self.Mission_statement)

    # Checks that technogies nav bar test is showing and hovers over the text
    def hover_over_top_technologies(self):
        self.hover_over_element(self.Technologies_dropdown)

    # Checks that technogies nav bar test is showing and hovers over the text
    def hover_over_top_company(self):
        self.hover_over_element(self.Company_dropdown)

    def check_for_nav_bar_technologies_link_text_options(self):
        for i in self.Technology_Nav_list:
            self.check_if_enabled(i)

    def check_for_nav_bar_company_link_text_options(self):
        for i in self.Company_Nav_list:
            self.check_if_enabled(i)

    def check_for_nav_contact_text(self):
        self.check_if_enabled(self.Nav_bar_Contact)

    def check_if_technology_drop_active(self):
        # return_css_property_value
        value = self.return_css_property_value(by_locator=self.Technology_dropdown_element, key="visibility")
        assert value == 'visible'

    def check_if_company_drop_active(self):
        # return_css_property_value
        value = self.return_css_property_value(by_locator=self.Company_dropdown_element, key="visibility")
        assert value == 'visible'



