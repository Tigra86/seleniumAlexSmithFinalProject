import datetime
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Method assert URL
    def assert_url(self, url):
        assert url == self.driver.current_url, f"Wrong URL: {self.driver.current_url}"
        print("")
        print(f"Current URL is correct: {url}")

    # Method assert page title
    def assert_page_title(self, page_title):
        assert page_title == self.driver.title, f"Wrong page title is displaying: {self.driver.title}"
        print(f"Correct page title is displaying: {page_title}")

    # Method assert checkbox is selected
    def assert_checkbox_is_selected(self, locator):
        self.driver.find_element(*locator).is_selected(), f"Checkbox is not selected"
        print("Checkbox is selected")

    # Method take screenshot
    def take_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f"screenshot-{now_date}.png"
        self.driver.save_screenshot(f"{os.getcwd()}/screen/{name_screenshot}")
        print("Screenshot is taken")

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))
