from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from handy_wrappers import HandyWrapper


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        hw = HandyWrapper(self.driver)
        self.driver.get("https://letskodeit.teachable.com/p/practice")
        hw.get_element("cars", by="name")
        self.driver.quit()





ff = RunChromeTests()
ff.test()
