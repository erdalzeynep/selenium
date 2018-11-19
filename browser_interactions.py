from selenium import webdriver
import os

class BrowserInteractions():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):


       # self.driver.maximize_window() doesnt work?
        self.driver.get("https://letskodeit.teachable.com/p/practice")
        title = self.driver.title
        current_url = self.driver.current_url

        print("Current url: " +current_url)
        print("Title: " +title)

        self.driver.refresh()
        print("first refresh")

        self.driver.refresh()
        print("Second refresh")

        self.driver.get("https://google.com")

        self.driver.back()
        print("One step back in browser")

        self.driver.forward()
        print("One step forward ")

        self.driver.quit()


ff = BrowserInteractions()
ff.test()
