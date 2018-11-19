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
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, -2000)")
        time.sleep(2)
        element = self.driver.find_element_by_id("mousehover")
        self.driver.execute_script("return arguments[0].scrollIntoView(false);",
                                   element)  # false sebebi bottoma scroll yapılması. eger top olsaydı true olmalıydı
        time.sleep(4)

        self.driver.quit()


ff = ScrollElement()
ff.test()
