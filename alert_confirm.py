from selenium import webdriver
import os
import time


class ScrollElement(object):
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.implicitly_wait(.5)
        self.driver.get("https://letskodeit.teachable.com/p/practice")
        self.driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        time.sleep(2)
        self.driver.quit()




ff = ScrollElement()
ff.test()
