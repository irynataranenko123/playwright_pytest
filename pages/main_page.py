from playwright.sync_api import Page, expect


class Main:

    def __init__(self, page: Page):

        self.page = page
        self.__body = self.page.locator('body')
        self.__login_btn = self.page.locator('[href="/login"]')
        self.__logged_in_text = self.page.locator('[class ="nav navbar-nav"]:last-child')
        self.__delete_account_btn = self.page.locator('[href="/delete_account"]')
        self.__logout_btn = self.page.locator('[href="/logout"]')
        self.__contact_us_btn = self.page.locator('[href="/contact_us"]')
        self.__test_cases_btn = self.page.locator('[href="/test_cases"]>[class="fa fa-list"]')
        self.__products_btn = self.page.locator('[href="/products"]')
        self.__footer = self.page.locator('[class="footer-widget"]')
        self.__subscription_text = self.page.locator('[class="single-widget"]>h2')
        self.__email_field = self.page.locator('[id="susbscribe_email"]')
        self.__subscribe_btn = self.page.locator('[id="subscribe"]')
        self.__successful_subscribe_msg = self.page.locator('[class="alert-success alert"]')
        self.__cart_btn = self.page.locator('[class="nav navbar-nav"]>li>[href="/view_cart"]')
        self.__continue_shopping_btn = self.page.locator('[data-dismiss="modal"]')
        self.__categories = self.page.locator('[class="panel-group category-products"]')
        self.__women_category = self.page.locator('[href="#Women"]')
        self.__men_category = self.page.locator('[href="#Men"]')
        self.__recommended_items = self.page.locator('[class="item active"]>:nth-child(1)>[class="product-image-wrapper"]'
                                                     '>[class="single-products"]>[class="productinfo text-center"]>'
                                                     '[class="btn btn-default add-to-cart"]')
        self.__scroll_up_arrow_btn = self.page.locator('[class="fa fa-angle-up"]')
        self.__main_text = self.page.locator('[class="item active"]>[class="col-sm-6"]>h2')

    def check_page_is_visible(self) -> None:
        expect(self.__body).to_be_visible()

    def click_login_btn(self) -> None:
        self.__login_btn.click()

    def check_logged_in_text_is_visible(self, name) -> None:
        self.__logged_in_text.wait_for(state='visible')
        expect(self.__logged_in_text).to_contain_text(f' Logged in as {name}')

    def delete_account(self) -> None:
        self.__delete_account_btn.click()

    def click_logout_btn(self) -> None:
        self.__logout_btn.click()
        expect(self.page).to_have_url('https://automationexercise.com/login')

    def click_contact_us_btn(self) -> None:
        self.__contact_us_btn.click()

    def click_test_cases_btn(self) -> None:
        self.__test_cases_btn.click()
        expect(self.page).to_have_url('https://automationexercise.com/test_cases')

    def click_products_btn(self) -> None:
        self.__products_btn.click()

    def scroll_to_footer(self) -> None:
        self.__footer.scroll_into_view_if_needed()
        self.__subscription_text.wait_for(state='visible')
        expect(self.__subscription_text).to_contain_text('Subscription')

    def fill_email_field(self, email) -> None:
        self.__email_field.type(email)

    def click_subscribe_btn(self) -> None:
        self.__subscribe_btn.click()

    def check_successful_subscribe_msg_is_visible(self) -> None:
        self.__successful_subscribe_msg.wait_for(state='visible')
        expect(self.__successful_subscribe_msg).to_contain_text('You have been successfully subscribed')

    def click_cart_btn(self) -> None:
        self.__cart_btn.click()
        expect(self.page).to_have_url('https://automationexercise.com/view_cart')

    def view_product_details(self, number) -> None:
        view_details = self.page.locator(f'[href="/product_details/{number}"]')
        view_details.click()
        expect(self.page).to_have_url(f'https://automationexercise.com/product_details/{number}')

    def add_product_to_cart(self, number) -> None:
        product_img = self.page.locator(f'[src="/get_product_picture/{number}"]')
        product_img.hover()
        add_to_cart_hovered_btn = self.page.locator(f'[class="overlay-content"]>[data-product-id="{number}"]')
        add_to_cart_hovered_btn.click()
        self.__continue_shopping_btn.click()

    def check_categories_is_visible(self) -> None:
        self.__categories.wait_for(state='visible')

    def choose_women_category(self) -> None:
        self.__women_category.click()

    def choose_subcategory(self, number) -> None:
        subcategory = self.page.locator(f'[href="/category_products/{number}"]')
        subcategory.click()

    def check_filter_text(self, gender, name) -> None:
        filter_text = self.page.locator('[class="features_items"]>h2')
        filter_text.wait_for(state='visible')
        expect(filter_text).to_contain_text(f'{gender} - {name} Products')

    def choose_men_category(self) -> None:
        self.__men_category.click()

    def scroll_to_recommended_items(self) -> None:
        self.__recommended_items.scroll_into_view_if_needed()
        self.__recommended_items.wait_for(state='visible')

    def add_to_cart_recommended_item(self) -> None:
        self.__recommended_items.click()
        self.__continue_shopping_btn.click()

    def scroll_up_by_arrow(self) -> None:
        self.__scroll_up_arrow_btn.click()
        self.__main_text.wait_for(state='visible')
        expect(self.__main_text).to_contain_text('Full-Fledged practice website for Automation Engineers')

    def scroll_up(self) -> None:
        self.__main_text.scroll_into_view_if_needed()
        self.__main_text.wait_for(state='visible')
        expect(self.__main_text).to_contain_text('Full-Fledged practice website for Automation Engineers')