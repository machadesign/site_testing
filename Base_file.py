import pytest


@pytest.mark.usefixtures("return_driver")
#  request.cls.driver = driver
# driver instance called , base_page  self.driver = driver
# login_page inherits driver from base_page
# call class to access it's variables / inherit from it within other pages
# access the driver object  ( request.cli.driver from the return_driver function in the conftest file )
class BasicTest:
    pass