from behave import *
from selenium import webdriver
from constants.globalconstants import *
from utilities.driver import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.login import *


@given('sahibinden sitesine gider')
def sahibinden_sitesine_gider(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(BASE_URL)
    
       


@given('sahibinden logosu goruntulenir')
def sahibinden_logosu_goruntulenir(context):
    logo=context.driver.find_element(By.CLASS_NAME,LOGO).is_displayed()
    assert logo is True
    

@then('giris yap tiklar')
def giris_yap_tiklar(context):
    pass