import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from constants.globalconstants import *


@pytest.mark.usefixtures("setup")
class Giris(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
