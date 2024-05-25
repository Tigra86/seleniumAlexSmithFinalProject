from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    wallets_link = ("id", "1_wallets_all-wallets")

    # Getters
    def get_wallets_link(self):
        return self.is_clickable(self.wallets_link)

    # Actions
    def click_wallets_link(self):
        self.get_wallets_link().click()
        print("Click Wallets link")

    # Methods
    def visit_wallets_page(self):
        self.assert_url("https://bellroy.com/")
        self.assert_page_title("Bellroy | Considered Carry Goods: Wallets, Bags, Phone Cases & More")
        self.click_wallets_link()
        self.take_screenshot()
