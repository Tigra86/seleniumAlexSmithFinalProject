from base.base_class import Base


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Actions

    # Methods
    def verify_checkout_page(self):
        self.assert_url("https://bellroy.com/checkout")
        self.assert_page_title("Checkout | Bellroy")
        self.take_screenshot()
