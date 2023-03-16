from playwright.sync_api import Page, expect


class ProductDetails:

    def __init__(self, page: Page):
        self.page = page
        self.__quantity = self.page.locator('[id="quantity"]')
        self.__add_to_cart_btn = self.page.locator('[class="btn btn-default cart"]')
        self.__view_cart_btn = self.page.locator('[class="text-center"]>[href="/view_cart"]')
        self.__write_review_text = self.page.locator('[href="#reviews"]')
        self.__name_field = self.page.locator('[id="name"]')
        self.__email_field = self.page.locator('[id="email"]')
        self.__review_field = self.page.locator('[id="review"]')
        self.__submit_btn = self.page.locator('[id="button-review"]')
        self.__successful_msg = self.page.locator('[class="col-md-12 form-group"]')

    def change_quantity(self, quantity) -> None:
        self.__quantity.clear()
        self.__quantity.type(quantity)

    def click_add_to_cart_btn(self) -> None:
        self.__add_to_cart_btn.click()

    def click_view_cart_btn(self) -> None:
        self.__view_cart_btn.click()

    def check_write_review_is_visible(self) -> None:
        self.__write_review_text.wait_for(state='visible')
        expect(self.__write_review_text).to_contain_text('Write Your Review')

    def fill_name_field(self, name) -> None:
        self.__name_field.type(name)

    def fill_email_field(self, email) -> None:
        self.__email_field.type(email)

    def fill_review_field(self, review) -> None:
        self.__review_field.type(review)

    def click_submit_btn(self) -> None:
        self.__submit_btn.click()

    def check_successful_msg_is_visible(self) -> None:
        self.__successful_msg.wait_for(state='visible')
        expect(self.__successful_msg).to_contain_text('Thank you for your review.')
