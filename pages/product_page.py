from base.base_class import Base
from utilities.logger import Logger
import allure
import time


class ProductPage(Base):
    # Locators
    add_to_cart_btn = ("xpath", "//button[@class='AddToCart HtmlProductAddToCart br_my-4 ']")
    checkout_btn = ("xpath", "/html/body/bellroy-minicart-slider/bellroy-checkout/div/div/div[3]/a")

    # Getters
    def get_add_to_cart_button(self):
        return self.is_clickable(self.add_to_cart_btn)

    def get_checkout_button(self):
        return self.is_clickable(self.checkout_btn)

    # Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()

    def click_checkout_button(self):
        self.get_checkout_button().click()

    # Methods
    def add_to_cart_and_checkout(self):
        with allure.step("Add product to cart and click Checkout button"):
            Logger.add_start_step(method="add_to_cart_and_checkout")
            self.assert_url("https://bellroy.com/products/travel-folio?color=caramel&material=leather_rfid")
            self.assert_page_title("Travel Folio | Zip Leather Passport Holder for Travel | Bellroy")
            self.click_add_to_cart_button()
            self.click_checkout_button()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_and_checkout")
