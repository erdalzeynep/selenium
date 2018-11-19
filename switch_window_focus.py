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
        print("Parent Handle: "+str(self.driver.current_window_handle))
        parent_handle = self.driver.current_window_handle
        button = self.driver.find_element_by_id("openwindow")
        button.click()
        handles = self.driver.window_handles
        print("All Open Handles: "+str(handles))
        self.driver.switch_to.window(handles[1])

        search_button = self.driver.find_element_by_id("search-courses")
        search_button.send_keys("ara")
        time.sleep(2)
        self.driver.switch_to.window(parent_handle)
        print("Current Handle: "+self.driver.current_window_handle)
        self.driver.find_element_by_id("name").send_keys("test")
        time.sleep(2)
        self.driver.quit()


ff = ScrollElement()
ff.test()
