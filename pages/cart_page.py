import re

from playwright.sync_api import Page, expect
from pages.products_page import Products


class Cart:

    def __init__(self, page: Page):

        self.page = page
        self.__all_products = self.page.locator('tbody')
        self.__product_price = self.page.locator('[id="product-1"]')
        self.products = Products(self.page)
        self.logo = self.page.locator('[src="/static/images/home/logo.png"]')
        self.__checkout_btn = self.page.locator('[class="btn btn-default check_out"]')
        self.__register_login_btn = self.page.locator('[class="text-center"]>[href="/login"]')
        self.__delete_product_btn = self.page.locator('[class="cart_quantity_delete"]')
        self.__empty_cart_text = self.page.locator('[id="empty_cart"]')

    def check_products_are_exist(self) -> None:
        self.__all_products.wait_for(state='visible')

    def check_product_is_in_cart(self, number) -> None:
        product = self.page.locator(f'[id="product-{number}"]')
        product.wait_for(state='visible')

    def check_product_price(self, number) -> None:
        prod_price = self.page.locator(f'[id="product-{number}"]>[class="cart_price"]>p')
        price2 = prod_price.get_attribute('text')
        quest = price2 == self.products.check_product_price(1)
        if quest:
            self.logo.click()

    def check_quantity(self, number, quantity) -> None:
        product_quantity = self.page.locator(f'[id="product-{number}"]>[class="cart_quantity"]')
        expect(product_quantity).to_have_text(quantity)

    def click_checkout_btn(self) -> None:
        self.__checkout_btn.click()

    def click_register_login_btn(self) -> None:
        self.__register_login_btn.click()

    def delete_product(self) -> None:
        self.__delete_product_btn.click()

    def check_cart_is_empty(self) -> None:
        self.__empty_cart_text.wait_for(state='visible')
        expect(self.__empty_cart_text).to_contain_text('Cart is empty!')

    def get_product_price(self, number) -> int:
        product_price = self.page.locator(f'[id="product-{number}"]>[class="cart_price"]>p')
        price_str = product_price.text_content()
        price_str = price_str.replace('Rs.', '')
        return int(price_str)

    def check_product_count(self, number) -> None:
        product_count = self.page.locator('[id*="product-"]')
        expect(product_count).to_have_count(number)

    def check_total_price(self, number) -> None:
        product_price = self.page.locator(f'[id="product-{number}"]>[class="cart_price"]>p')
        price_str = product_price.text_content()
        price_str = price_str.replace('Rs.', '')
        price_int = int(price_str)
        total_price = self.page.locator(f'[id="product-{number}"]>[class="cart_total"]>p')
        total_str = total_price.text_content()
        total_str = total_str.replace('Rs.', '')
        total_int = int(total_str)
        total_count = self.page.locator(f'[id="product-{number}"]>[class="cart_quantity"]>button')
        count_str = total_count.text_content()
        count_int = int(count_str)
        assert total_int == price_int*count_int