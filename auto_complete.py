from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AutoCompleteExample():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.implicitly_wait(.5)
        self.driver.get("https://www.southwestvacations.com/")
        element = self.driver.find_element_by_xpath("//div[@class='selectize-control single plugin-accessibility plugin-item_nowrap plugin-typeOver'][1]")
        time.sleep(2)
        element.click()
        destination = self.driver.find_element_by_id("ctl00_ContentPlaceHolder_RestoolComponent_Origin_SelectizeInput")
        destination.click()
        destination.send_keys("bo")
        time.sleep(2)
        city_selection = self.driver.find_element_by_xpath(
            "//div[@id='ctl00_ContentPlaceHolder_RestoolComponent_Origin_SelectizeContainer']//div[@data-value='Boston (BOS)']")
        city_selection.click()


ff = AutoCompleteExample()
ff.test()
