from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ClickAndSendKey():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.get("https://letskodeit.teachable.com/p/practice")
        select_element = self.driver.find_element_by_id("carselect")
        select = Select(select_element)
        #time.sleep(3)
        select.select_by_value("benz")


ff = ClickAndSendKey()
ff.test()
