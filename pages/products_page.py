from _pytest.outcomes import fail
from playwright.sync_api import Page, expect


class Products:

    def __init__(self, page: Page):

        self.page = page
        self.__main_text = self.page.locator('[class="features_items"]>h2')
        self.__products_list = self.page.locator('[class="features_items"]')
        self.__product_information = self.page.locator('[class="product-information"]')
        self.__search_field = self.page.locator('[id="search_product"]')
        self.__search_btn = self.page.locator('[id="submit_search"]')
        self.__product_info = self.page.locator('[class="productinfo text-center"]')
        self.__continue_shopping_btn = self.page.locator('[data-dismiss="modal"]')
        self.__brands = self.page.locator('[class="brands-name"]')
        self.__brand_polo = self.page.locator('[href="/brand_products/Polo"]')
        self.__brands_text = self.page.locator('[class="features_items"]>h2')
        self.__brand_madame = self.page.locator('[href="/brand_products/Madame"]')

    def check_all_products_is_visible(self) -> None:
        self.__main_text.wait_for(state='visible')
        expect(self.__main_text).to_contain_text('All Products')

    def check_product_list_is_visible(self) -> None:
        self.__products_list.wait_for(state='visible')

    def view_product_information(self, number) -> None:
        view_product = self.page.locator(f'[href="/product_details/{number}"]')
        view_product.click()
        expect(self.page).to_have_url('https://automationexercise.com/product_details/1')

    def check_product_information_is_visible(self) -> None:
        self.__product_information.wait_for(state='visible')

    def search_product(self, product) -> None:
        self.__search_field.type(product)
        self.__search_btn.click()

    def check_searched_products_is_visible(self) -> None:
        self.__main_text.wait_for(state='visible')
        expect(self.__main_text).to_contain_text('Searched Products')

    def add_product_to_cart(self, number) -> None:
        product_img = self.page.locator(f'[src="/get_product_picture/{number}"]')
        product_img.hover()
        add_to_cart_hovered_btn = self.page.locator(f'[class="overlay-content"]>[data-product-id="{number}"]')
        add_to_cart_hovered_btn.click()
        self.__continue_shopping_btn.click()

    def get_product_price(self, number) -> int:
        product_price = self.page.locator(f'[src="/get_product_picture/{number}"]~h2')
        price_str = product_price.text_content()
        price_str = price_str.replace('Rs.', '')
        return int(price_str)

    def check_brands_is_visible(self) -> None:
        self.__brands.wait_for(state='visible')

    def choose_brand_polo(self) -> None:
        self.__brand_polo.click()
        expect(self.page).to_have_url('https://automationexercise.com/brand_products/Polo')

    def check_brands_text_is_visible(self, name) -> None:
        self.__brands_text.wait_for(state='visible')
        expect(self.__brands_text).to_contain_text(f'Brand - {name} Products')

    def choose_brand_madame(self) -> None:
        self.__brand_madame.click()
        expect(self.page).to_have_url('https://automationexercise.com/brand_products/Madame')

