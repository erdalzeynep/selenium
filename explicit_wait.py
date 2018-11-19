from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time



class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.implicitly_wait(.5)
        self.driver.get("https://www.expedia.com/")

        self.driver.find_element_by_id("tab-flight-tab-hp").click()
        source_element = self.driver.find_element_by_xpath(
            "//input[@class='clear-btn-input gcw-storeable text gcw-origin gcw-required gcw-distinct-locations ']")
        time.sleep(1)
        source_element.send_keys("SFO")
        self.driver.find_element_by_xpath("//a[@id='aria-option-0']//div[@class='multiLineDisplay']").click()

        nyc_element = self.driver.find_element_by_xpath(
            "//input[@class='clear-btn-input gcw-storeable text gcw-destination gcw-required gcw-distinct-locations ']")
        time.sleep(1)
        nyc_element.send_keys("NYC")
        self.driver.find_element_by_xpath("//a[@id='aria-option-0']//div[@class='multiLineDisplay']").click()

        self.driver.find_element_by_id("flight-returning-hp-flight").send_keys("11/24/2018")
        self.driver.find_element_by_id("flight-departing-hp-flight").send_keys("10/28/2018")
        self.driver.find_element_by_xpath("//div[@id='flight-departing-wrapper-hp-flight']//button[contains(@class, 'datepicker-close-btn')]").click()

        # self.driver.find_element_by_id("flight-departing-hp-flight").send_keys(Keys.ENTER)

        self.driver.find_element_by_css_selector("#gcw-flights-form-hp-flight [type='submit']").click()

        wait = WebDriverWait(self.driver, 25, poll_frequency=1)
        element = wait.until(expected_conditions.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

ff = RunChromeTests()
try:
    ff.test()
finally:
    input("Type something to quit...")
    ff.driver.quit()
