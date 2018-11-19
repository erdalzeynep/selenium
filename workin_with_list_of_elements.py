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
        radio_button_lists = self.driver.find_elements_by_xpath(
            "//div[@id='radio-btn-example']//input[contains(@type,'radio')]")

        size_of_list = len(radio_button_lists)
        print("Radio button count : " + str(size_of_list))



        for radio_button in radio_button_lists:
            if radio_button.is_selected() is False:
                radio_button.click()
                print("selected radio button location: " + str(radio_button.location))
                exit()

ff = ClickAndSendKey()
ff.test()
