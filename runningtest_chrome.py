from selenium import webdriver
import os

from selenium.webdriver.common.by import By


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__) 
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.get("https://letskodeit.teachable.com/p/practice")
        element_by_id = self.driver.find_element(By.ID, "carselect")

        if element_by_id is not None:
            print("we found element by id")

        # finding multiple elements

        element_list_by_classname = self.driver.find_elements_by_class_name("inputs")
        length = len(element_list_by_classname)
        print("size of class list is: " + str(length))

        element_open_tab = self.driver.find_element_by_id("opentab")
        open_tab_text = element_open_tab
        print("text: " + str(open_tab_text))


ff = RunChromeTests()
ff.test()
