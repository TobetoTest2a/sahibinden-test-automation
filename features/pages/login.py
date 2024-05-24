# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions


# LOGO="logo"  #class NAME

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.sahibinden.com"
        self.search_box = (By.ID, "searchText")
        self.search_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        self.driver.get(self.url)

    def enter_search_term(self, term):
        search_box_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box)
        )
        search_box_element.clear()
        search_box_element.send_keys(term)

    def click_search_button(self):
        search_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        )
        search_button_element.click()
