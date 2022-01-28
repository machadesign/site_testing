# conftest to provide fixtures to tests within it's own directory

import yaml
import time
import pytest
import re
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireServcie
# Service - Manages the life and death of a ChromeDriver server.


with open("/Users/matthewchadwell/Library/Preferences/PyCharmCE2019.1/scratches/scratch.yml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

list_of_environments = data["BROWSER_PARAMS"]
chrome_path_exe = data["BROWSER_EXE_PATHS"]["CHROME"]
firefox_path_exe = data["BROWSER_EXE_PATHS"]["FIREFOX"]
safari_path_exe = data["BROWSER_EXE_PATHS"]["SAFARI"]


# if need to change yaml values
screen_size = "SCREEN_SIZE"
headless = "HEADLESS"
# full_screen = "FULLSCREEN"
browser_width = "SCREEN_WIDTH"
browser_height = "SCREEN_HEIGHT"

Cservice = ChromeService(executable_path=chrome_path_exe)
Fservice = FireServcie(executable_path=firefox_path_exe)


def check_device_list_for_device_type(request_param):
    # list alredy being looped through
    regex = r"mobile_([A-Za-z0-9+/ ]*)"

    # device must be installed chrome browser first
    param_string = str(request_param)
    if re.search("mobile", param_string):
        browser_type = "MOBILE"
        # mobile device name from defined name in config file (ex: mobile_Nexus 5 - Nexus 5)
        result = re.search(regex, param_string)
        mobile_device = str(result[1]).rstrip()
        # device:mobile name , browser_type:MOBILE
        return mobile_device, browser_type
    else:
        browser_name = param_string.rstrip().upper()
        browser_type = "RESPONSIVE"
        return browser_name, browser_type

# pytest is the global fixture
@pytest.fixture(params=list_of_environments, scope="class")
# class multiple test cases will get called and drive ronly called once
# function , driver is called for each test case in a class
def return_driver(request):
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()

    device_or_browser_name = check_device_list_for_device_type(request.param)
    # returns the name of browser / mobile device name

    name, type = device_or_browser_name

    # try:
    if name == "CHROME":
        # data['CHROME']['CHROME_HEADLESS']
        if data[name][headless]:
            # is True:
            chrome_options.add_argument('--headless')
        if data[name][screen_size] == "FULLSCREEN":
            # --start-maximized 	Starts the browser maximized, regardless of any previous settings.
            chrome_options.add_argument("--start-fullscreen")
        else:
            # Custom browser size width/height set
            window_size = "window-size={},{}".format(data[name][browser_width], data[name][browser_height])
            chrome_options.add_argument(window_size)
        web_driver = webdriver.Chrome(service=Cservice, options=chrome_options)

    if name == "FIREFOX":
        if data[name][headless]:
            # is True:
            firefox_options.add_argument('--headless')
        ''' Firefox does not currently have a command for full screen , the if statement needs to be performed last
        instance of webdriver needed '''
        if data[name][screen_size] == "FULLSCREEN":
            # --start-maximized 	Starts the browser maximized, regardless of any previous settings.
            web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
            web_driver.maximize_window()
            # firefox_options.add_argument("-fullscreen")
            # firefox_options.add_argument("--start-fullscreen")
        else:
            firefox_options.add_argument("--width={}".format(data[name][browser_width]))
            firefox_options.add_argument("--height={}".format(data[name][browser_height]))
            web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
        # web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
    #
    if name == "SAFARI":
        # Headless not available for safari
        # Safari’s WebDriver support for developers is turned off by default
        if data[name][screen_size] == "FULLSCREEN":
            # --start-maximized 	Starts the browser maximized, regardless of any previous settings.
            web_driver = webdriver.Safari(executable_path=safari_path_exe)
            web_driver.maximize_window()
        else:
            web_driver = webdriver.Safari(executable_path=safari_path_exe)
            web_driver.set_window_size(data[name][browser_width], data[name][browser_height])

    if type == "MOBILE":
        mobile_emulation = {"deviceName": name}
        # specify orientation the device
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        web_driver = webdriver.Chrome(service=Cservice, options=chrome_options)

    request.cls.driver = web_driver
    yield
    web_driver.close()

    # except Exception as e:
    #     print("Browser {} could not be accessed".format(name))

        #
        # width = 300
        # height = 300
        # web_driver = webdriver.Safari(options=)
        # web_driver.set_window_size(width, height)






#             option.add_argument("--width={}".format(data[data_width]))
        #             option.add_argument("--height={}".format(data[data_height]))







        # if name == "firefox":
        #     # bowser size either full or custom
        #     #  page_loading(firefox_options, name)
        #     browser_window_size(firefox_options, name)
        #     # does not work fro firefox
        #     # firefox_options.add_argument('--window-size=350,350')
        #     if data["FIREFOX_HEADLESS"] is False:
        #         # firefox_options.add_argument('--window-size=350,350')
        #
        #         web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
        #         # web_driver.set_window_size(200, 200)
        #     else:
        #         firefox_options.add_argument('--headless')
        #         web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
        #
        #     if data[data_name_size] == "FULLSCREEN":
        #         # --start-maximized 	Starts the browser maximized, regardless of any previous settings.
        #         chrome_options.add_argument("--start-fullscreen")
        #     else:
        #         chrome_options.add_argument("--width={}".format(data[data_width]))
        #         chrome_options.add_argument("--height={}".format(data[data_height]))
        #     web_driver = webdriver.Chrome(service=Cservice, options=chrome_options)

            #
            # if browser == "firefox":
            #     option.add_argument("--width={}".format(data[data_width]))
            #     option.add_argument("--height={}".format(data[data_height]))
            #


        # browser_window_size(chrome_options, name)
        # try:
        #
        # if data[data_headless] is False:
        #     web_driver = webdriver.Chrome(service=Cservice, options=chrome_options)
        # else:
        #     chrome_options.add_argument('--headless')
        #     web_driver = webdriver.Chrome(service=Cservice, options=chrome_options)


            # else:
            #     print("Incorrect selection for chrome browser, True or False required")
        # except NameError:
        #     print("whoaaa exeptiones")
        #     raise


        # except Exception as e:
        #   print("Browser {} could not be accessed")


# For Windows OS systems you need to add the argument --disable-gpu
#     if name == "headless_Chrome":
#         # NEVER going to run non headless and headless for same browser
#
#         # specify dictionary in config file   value normal or headless
#
#         # For Windows OS systems you need to add the argument --disable-gpu
#         screen_size = chrome_configs_frm_yaml()
#         # hrome_options.add_argument("--window-size=1920,1080")
#         chrome_options.add_argument(screen_size)
#         chrome_options.add_argument('--headless')
#         web_driver = webdriver.Chrome(service=Cservice, options=chrome_options)


    # if name == "firefox":
    #     # specify dictionary in config file   value normal or headless
    #     web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
    #
    #     # # For Windows OS systems you need to add the argument --disable-gpu
    # if name == "headless_Firefox":
    #     firefox_options.add_argument('--headless')
    #     screen_size = chrome_configs_frm_yaml()
    #     firefox_options.add_argument(screen_size)
    #
    #     web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
    # if name == "firefox":
    #    # bowser size either full or custom
    #    #  page_loading(firefox_options, name)
    #     browser_window_size(firefox_options, name)
    #    # does not work fro firefox
    #     # firefox_options.add_argument('--window-size=350,350')
    #     if data["FIREFOX_HEADLESS"] is False:
    #         # firefox_options.add_argument('--window-size=350,350')
    #
    #         web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)
    #         # web_driver.set_window_size(200, 200)
    #     else:
    #         firefox_options.add_argument('--headless')
    #         web_driver = webdriver.Firefox(service=Fservice, options=firefox_options)


    #
    #     if data[data_name_size] == "FULLSCREEN":
    #         # --start-maximized 	Starts the browser maximized, regardless of any previous settings.
    #         option.add_argument("--start-fullscreen")
    #     else:
    #         if browser == "chrome":
    #             window_size = "window-size={},{}".format(data[data_width], data[data_height])
    #             option.add_argument(window_size)
    #         if browser == "firefox":
    #             option.add_argument("--width={}".format(data[data_width]))
    #             option.add_argument("--height={}".format(data[data_height]))



    # chrome_options = webdriver.ChromeOptions()
    #
    # # Add the mobile emulation to the chrome options variable
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
    # self.driver = webdriver.Chrome(
    #     executable_path='/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver',
    #     chrome_options=chrome_options)

    #
    # if type == "mobile":
    #     options = ChromeOptions()
    #     mobile_emulation = {"deviceName": data[device_or_browser_name]}
    #     options.add_experimental_option("mobileEmulation", mobile_emulation)
    #     web_driver = webdriver.Chrome(service=service, options=options)
    # request.cls.driver = web_driver
    # yield
    # web_driver.close()

    #
    # else:
    #     raise Exception(f'Browser "{request.param}" is not supported')




    #
    # if request.param == "firefox":
    #     web_driver = webdriver.Chrome(service=service)
    #     web_driver.set_window_size(112, 1112)
    # #     # web_driver in request variable at a (scope=" ") level which can be accessed while running your test
    # #     request.cls.driver = driver
    # request.cls.driver = web_driver
    # # need to specificly specify web_driver , stores driver in webdriver object
    # yield
    # web_driver.close()

# specify window size

if __name__ == "__main__":
    # check_this()
    # check_firefox_browser_version()
    # check_chrome_browser_version()
    check_safari_browser_version()

