from base.base_class import Base
from utilities.logger import Logger
import allure


class CheckoutPage(Base):
    # Locators

    # Getters

    # Actions

    # Methods
    def verify_checkout_page(self):
        with allure.step("Verify Checkout page"):
            Logger.add_start_step(method="verify_checkout_page")
            self.assert_url("https://bellroy.com/checkout")
            self.assert_page_title("Checkout | Bellroy")
            self.take_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="verify_checkout_page")
