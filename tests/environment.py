

import getpass
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.safari.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest

from constants.globalconstants import *


@pytest.fixture(scope="function")
def setup():

    if browser is None:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "safari": #bu projede safari kullanilmadi, ornek icin konuldu
            service = Service("./drivers/safari")
            driver = webdriver.Chrome(service=service)
        else:
            print("Girdiginiz Browser Hatali!!")

   
    driver.get(BASE_URL)
    driver.maximize_window()
   # request.cls.driver = driver
   # request.cls.baseurl = base_url
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# def before_all(context):
#     context.driver = webdriver.Chrome(ChromeDriverManager().install())

# def after_all(context):
#     context.driver.quit()

    