from selenium import webdriver
import os
import time
from selenium.webdriver import ActionChains


class ScrollElement(object):
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.implicitly_wait(.5)
        self.driver.get("https://letskodeit.teachable.com/p/practice")
        action = ActionChains(self.driver)
        self.driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(2)
        element = self.driver.find_element_by_id("mousehover")
        action.move_to_element(element).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='mouse-hover']//a[text()='Top']").click()


ff = ScrollElement()
ff.test()
