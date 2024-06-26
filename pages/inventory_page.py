from base.base_class import Base
from utilities.logger import Logger
import allure
import time


class InventoryPage(Base):
    # Locators
    coins_checkbox = ("xpath", "//span[text()='Coins']")
    folded_bills_checkbox = ("xpath", "//span[text()='Folded bills']")
    cards_checkbox = ("xpath", "//span[text()='Cards']")
    item_card = ("xpath", "(//span[@class='br_absolute br_inset-0 br_z-10'])[2]")

    # Getters
    def get_coins_checkbox(self):
        return self.is_clickable(self.coins_checkbox)

    def get_folded_bills_checkbox(self):
        return self.is_clickable(self.folded_bills_checkbox)

    def get_cards_checkbox(self):
        return self.is_clickable(self.cards_checkbox)

    def get_item_card(self):
        return self.is_clickable(self.item_card)

    # Actions
    def select_filters(self):
        self.get_coins_checkbox().click()
        self.get_folded_bills_checkbox().click()
        self.get_cards_checkbox().click()
        print("Select multiple filters")

    def select_item(self):
        self.get_item_card().click()
        print("Select item")

    # Methods
    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method="select_product")
            self.assert_url("https://bellroy.com/products/category/wallets")
            self.assert_page_title("Slim Leather Wallets, Zip Wallets, Cardholders For Men & Women")
            self.select_filters()
            self.assert_checkbox_is_selected(self.coins_checkbox)
            self.assert_checkbox_is_selected(self.folded_bills_checkbox)
            self.assert_checkbox_is_selected(self.cards_checkbox)
            self.select_item()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="select_product")
