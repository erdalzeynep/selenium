from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By

class ClickAndSendKey():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self): 

        self.driver.get("https://letskodeit.teachable.com/p/practice")
        signup_link=self.driver.find_element_by_xpath("//a[@href='/sign_up']")
        signup_link.click()

        time.sleep(3)

        username_field= self.driver.find_element_by_id("user_name")
        print(str(username_field.is_enabled())) # check if the element is enable or disable
        username_field.send_keys("erdalzeynep")

        time.sleep(3)

        email_field=self.driver.find_element_by_id("user_email")
        email_field.send_keys("abcde")

        username_field.clear()




ff = ClickAndSendKey()
ff.test()
