from pages.main_page import MainPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
import allure


@allure.description("Buy product")
def test_buy_product(driver):
    driver = driver

    mp = MainPage(driver)
    mp.visit_wallets_page()

    ip = InventoryPage(driver)
    ip.select_product()

    pp = ProductPage(driver)
    pp.add_to_cart_and_checkout()

    cp = CheckoutPage(driver)
    cp.verify_checkout_page()