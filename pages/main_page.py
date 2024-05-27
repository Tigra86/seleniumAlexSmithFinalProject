from base.base_class import Base
from utilities.logger import Logger
import allure
import time


class MainPage(Base):
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
        with allure.step("Visit Wallets page"):
            Logger.add_start_step(method="visit_wallets_page")
            self.assert_url("https://bellroy.com/")
            self.assert_page_title("Bellroy | Considered Carry Goods: Wallets, Bags, Phone Cases & More")
            self.click_wallets_link()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="visit_wallets_page")
