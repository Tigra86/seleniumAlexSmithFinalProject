import time

from base.base_class import Base


class SearchResultPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sort_by_dropdown = ("id", "a-autoid-0")
    high_to_low_option = ("id", "s-result-sort-select_2")
    hanes_checkbox = ("xpath", "//*[@id='p_89/Hanes']/span/a/div/label/i")
    anrabess_checkbox = ("xpath", "//*[@id='p_89/ANRABESS']/span/a/div/label/i")
    product = ("xpath", "//div[@cel_widget_id='MAIN-SEARCH_RESULTS-4']")
    product_title = ("id", "productTitle")

    # Getters
    def get_sort_by_dropdown(self):
        return self.is_clickable(self.sort_by_dropdown)

    def get_high_to_low_option(self):
        return self.is_clickable(self.high_to_low_option)

    def get_hanes_checkbox(self):
        return self.is_visible(self.hanes_checkbox)

    def get_anrabess_checkbox(self):
        return self.is_visible(self.anrabess_checkbox)

    def get_product(self):
        return self.is_clickable(self.product)

    def get_product_title(self):
        return self.is_visible(self.product_title)

    # Actions
    def select_dropdown_option(self):
        self.get_sort_by_dropdown().click()
        self.get_high_to_low_option().click()
        print("Select drop-down option")

    def select_filters(self):
        self.get_hanes_checkbox().click()
        self.get_anrabess_checkbox().click()
        print("Select multiple filters")

    def select_item_text(self):
        return self.get_product().text

    def select_item(self):
        self.get_product().click()

    # Methods
    def select_product(self):
        self.select_dropdown_option()
        self.select_filters()
        self.select_item()
        self.take_screenshot()
