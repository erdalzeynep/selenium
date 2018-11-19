from selenium import webdriver
import os
import time


class CalendarExample(object):
    # http://chromedriver.storage.googleapis.com/index.html

    def __init__(self):
        container_folder = os.path.dirname(__file__)
        driver_location = container_folder + "/chromedriver"
        self.driver = webdriver.Chrome(driver_location)

    def test(self):
        self.driver.implicitly_wait(.5)
        self.driver.get("https://www.expedia.com/")
        self.driver.find_element_by_id("tab-flight-tab-hp").click()

        flight_date_field = self.driver.find_element_by_id("flight-departing-hp-flight")

        flight_date_field.click()
        time.sleep(2)
        day_element = self.driver.find_element_by_xpath(
            "(//table[@class='datepicker-cal-weeks'])[2]//button[@data-day='29']")
        day_element.click()
        time.sleep(2)
        self.take_screenshot()

        self.driver.quit()


    def take_screenshot(self):
        file_name = str(time.strftime("%Y%m%d-%H%M%S")) + ".png"
        file_path = "/Users/zeynepdal/Desktop/seleniumscreenshots/" + file_name
        self.driver.save_screenshot(file_path)


# there was a file name conflict on calendar

if __name__ == '__main__':
    ff = CalendarExample()
    ff.test()
