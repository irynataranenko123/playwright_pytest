import pytest

from pages.main_page import Main
from pages.login_page import Login
from pages.signup_page import SignUp
from pages.account_created_page import AccountCreated
from pages.account_deleted_page import AccountDeleted
from pages.contact_us_page import ContactUs
from pages.products_page import Products
from pages.cart_page import Cart
from pages.product_details_page import ProductDetails
from pages.checkout_page import Checkout
from pages.payment_page import Payment
from utils.test_data import Data
from utils.tools import take_screenshot


class TestCases:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        #self.page.set_viewport_size(viewport_size={'width': 1460, 'height': 600})
        self.login = Login(self.page)
        self.main = Main(self.page)
        self.signup = SignUp(self.page)
        self.account_created = AccountCreated(self.page)
        self.account_deleted = AccountDeleted(self.page)
        self.contact_us = ContactUs(self.page)
        self.products = Products(self.page)
        self.cart = Cart(self.page)
        self.product_details = ProductDetails(self.page)
        self.checkout = Checkout(self.page)
        self.payment = Payment(self.page)

        #self.page.goto(f'http://automationexercise.com/')

    def test_first(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.check_new_user_is_visible()
        self.login.fill_name(Data.username)
        self.login.fill_signup_email(Data.signup_email)
        self.login.click_sign_up_btn()
        self.signup.check_enter_information_is_visible()
        self.signup.select_radio_btn(Data.Mr)
        self.signup.fill_password(Data.password)
        self.signup.select_day(Data.day)
        self.signup.select_month(Data.month)
        self.signup.select_year(Data.year)
        self.signup.check_newsletter_checkbox()
        self.signup.check_special_offers_checkbox()
        self.signup.fill_first_name(Data.first_name)
        self.signup.fill_last_name(Data.last_name)
        self.signup.fill_company(Data.company)
        self.signup.fill_address_1(Data.address_1)
        self.signup.fill_address_2(Data.address_2)
        self.signup.select_country(Data.country)
        self.signup.fill_state(Data.state)
        self.signup.fill_city(Data.city)
        self.signup.fill_zipcode(Data.zipcode)
        self.signup.fill_mobile_number(Data.mobile_number)
        self.signup.click_create_account_btn()
        self.account_created.check_account_created_is_visible()
        self.account_created.click_continue_btn()
        self.main.check_logged_in_text_is_visible(Data.username)
        self.main.delete_account()
        self.account_deleted.check_account_deleted_is_visible()
        self.account_deleted.click_continue_btn()
        take_screenshot(self.page, 'test_first')

    def test_second(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.check_login_to_account_is_visible()
        self.login.fill_login_email(Data.login_email)
        self.login.fill_password(Data.password)
        self.login.click_login_btn()
        self.main.check_logged_in_text_is_visible(Data.test_username)
        take_screenshot(self.page, 'test_second')

    def test_third(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.check_login_to_account_is_visible()
        self.login.fill_login_email(Data.incorrect_email)
        self.login.fill_password(Data.incorrect_password)
        self.login.click_login_btn()
        self.login.check_error_invalid_data_msg_is_visible()
        take_screenshot(self.page, 'test_third')

    def test_fourth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.check_login_to_account_is_visible()
        self.login.fill_login_email(Data.login_email)
        self.login.fill_password(Data.password)
        self.login.click_login_btn()
        self.main.check_logged_in_text_is_visible(Data.test_username)
        self.main.click_logout_btn()
        take_screenshot(self.page, 'test_fourth')

    def test_fifth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.check_new_user_is_visible()
        self.login.fill_name(Data.username)
        self.login.fill_signup_email(Data.login_email)
        self.login.click_sign_up_btn()
        take_screenshot(self.page, 'test_fifth')

    def test_sixth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_contact_us_btn()
        self.contact_us.check_get_in_touch_is_visible()
        self.contact_us.fill_name(Data.username)
        self.contact_us.fill_email(Data.signup_email)
        self.contact_us.fill_subject(Data.subject)
        self.contact_us.fill_message(Data.message)
        self.contact_us.upload_file()
        self.contact_us.click_submit_btn()
        self.contact_us.click_submit_btn()
        self.contact_us.check_successful_msg_is_visible()
        take_screenshot(self.page, 'test_sixth')

    def test_seventh(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_test_cases_btn()
        take_screenshot(self.page, 'test_seventh')

    def test_eighth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_products_btn()
        self.products.check_all_products_is_visible()
        self.products.check_product_list_is_visible()
        self.products.view_product_information(1)
        self.products.check_product_information_is_visible()
        take_screenshot(self.page, 'test_eighth')

    def test_ninth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_products_btn()
        self.products.check_all_products_is_visible()
        self.products.search_product(Data.product)
        self.products.check_searched_products_is_visible()
        self.products.check_product_list_is_visible()
        take_screenshot(self.page, 'test_ninth')

    def test_tenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.scroll_to_footer()
        self.main.fill_email_field(Data.login_email)
        self.main.click_subscribe_btn()
        self.main.check_successful_subscribe_msg_is_visible()
        take_screenshot(self.page, 'test_tenth')

    def test_eleventh(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_cart_btn()
        self.main.scroll_to_footer()
        self.main.fill_email_field(Data.login_email)
        self.main.click_subscribe_btn()
        self.main.check_successful_subscribe_msg_is_visible()
        take_screenshot(self.page, 'test_eleventh')

    def test_twelfth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_products_btn()
        initial_price_1 = self.products.get_product_price(1)
        initial_price_2 = self.products.get_product_price(2)
        self.products.add_product_to_cart(1)
        self.products.add_product_to_cart(2)
        self.main.click_cart_btn()
        self.cart.check_product_is_in_cart(1)
        self.cart.check_product_is_in_cart(2)
        cart_price_1 = self.cart.get_product_price(1)
        cart_price_2 = self.cart.get_product_price(2)
        assert cart_price_1 == initial_price_1, f"Expected initial price {initial_price_1} is not equal to cart " \
                                                f"price {cart_price_1}"
        assert cart_price_2 == initial_price_2, f"Expected initial price {initial_price_2} is not equal to cart " \
                                                f"price {cart_price_2}"
        self.cart.check_product_count(2)
        self.cart.check_total_price(1)
        self.cart.check_total_price(2)
        take_screenshot(self.page, 'test_twelfth')

    def test_thirteenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.view_product_details(1)
        self.product_details.change_quantity('4')
        self.product_details.click_add_to_cart_btn()
        self.product_details.click_view_cart_btn()
        self.cart.check_quantity(1, '4')
        take_screenshot(self.page, 'test_thirteenth')

    def test_fourteenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.cart.click_register_login_btn()
        self.login.fill_name(Data.username)
        self.login.fill_signup_email(Data.signup_email)
        self.login.click_sign_up_btn()
        self.signup.create_new_account(Data.Mr, Data.password, Data.day, Data.month, Data.year, Data.first_name,
                                       Data.last_name, Data.company, Data.address_1, Data.address_2, Data.country,
                                       Data.city, Data.state, Data.zipcode, Data.mobile_number)
        self.account_created.check_account_created_is_visible()
        self.account_created.click_continue_btn()
        self.main.check_logged_in_text_is_visible(Data.username)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.checkout.check_address_details_is_visible()
        self.checkout.review_order(1)
        self.checkout.add_comment(Data.comment)
        self.checkout.place_order()
        self.payment.add_card_information(Data.card_name, Data.card_number, Data.cvc, Data.expiry_month,
                                          Data.expiry_year)
        self.payment.click_pay_btn()
        self.payment.check_successful_msg_is_visible()
        self.main.delete_account()
        self.account_deleted.check_account_deleted_is_visible()
        self.account_deleted.click_continue_btn()
        take_screenshot(self.page, 'test_fourteenth')

    def test_fifteenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.fill_name(Data.username)
        self.login.fill_signup_email(Data.signup_email)
        self.login.click_sign_up_btn()
        self.signup.create_new_account(Data.Mr, Data.password, Data.day, Data.month, Data.year, Data.first_name,
                                       Data.last_name, Data.company, Data.address_1, Data.address_2, Data.country,
                                       Data.city, Data.state, Data.zipcode, Data.mobile_number)
        self.account_created.check_account_created_is_visible()
        self.account_created.click_continue_btn()
        self.main.check_logged_in_text_is_visible(Data.username)
        self.main.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.checkout.check_delivery_address_information(Data.first_name, Data.last_name, Data.company, Data.address_1,
                                                         Data.address_2, Data.city, Data.state, Data.zipcode,
                                                         Data.country, Data.mobile_number)
        self.checkout.review_order(1)
        self.checkout.add_comment(Data.comment)
        self.checkout.place_order()
        self.payment.add_card_information(Data.card_name, Data.card_number, Data.cvc, Data.expiry_month,
                                          Data.expiry_year)
        self.payment.click_pay_btn()
        self.payment.check_successful_msg_is_visible()
        self.main.delete_account()
        self.account_deleted.check_account_deleted_is_visible()
        self.account_deleted.click_continue_btn()
        take_screenshot(self.page, 'test_fifteenth')

    def test_sixteenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.fill_login_email(Data.login_email)
        self.login.fill_password(Data.password)
        self.login.click_login_btn()
        self.main.check_logged_in_text_is_visible(Data.test_username)
        self.main.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.checkout.check_delivery_address_information(Data.first_name, Data.last_name, Data.company, Data.address_1,
                                                         Data.address_2, Data.city, Data.state, Data.zipcode,
                                                         Data.country, Data.mobile_number)
        self.checkout.review_order(1)
        self.checkout.add_comment(Data.comment)
        self.checkout.place_order()
        self.payment.add_card_information(Data.card_name, Data.card_number, Data.cvc, Data.expiry_month,
                                          Data.expiry_year)
        self.payment.click_pay_btn()
        self.payment.check_successful_msg_is_visible()
        take_screenshot(self.page, 'test_sixteenth')

    def test_seventeenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.delete_product()
        self.cart.check_cart_is_empty()
        take_screenshot(self.page, 'test_seventeenth')

    def test_eighteenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.check_categories_is_visible()
        self.main.choose_women_category()
        self.main.choose_subcategory(1)
        self.main.check_filter_text('Women', 'Dress')
        self.main.choose_men_category()
        self.main.choose_subcategory(3)
        self.main.check_filter_text('Men', 'Tshirts')
        take_screenshot(self.page, 'test_eighteenth')

    def test_nineteenth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_products_btn()
        self.products.check_brands_is_visible()
        self.products.choose_brand_polo()
        self.products.check_brands_text_is_visible('Polo')
        self.products.choose_brand_madame()
        self.products.check_brands_text_is_visible('Madame')
        take_screenshot(self.page, 'test_nineteenth')

    def test_twentieth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_products_btn()
        self.products.check_all_products_is_visible()
        self.products.search_product(Data.product)
        self.products.check_searched_products_is_visible()
        self.products.check_product_list_is_visible()
        self.products.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.check_product_is_in_cart(1)
        self.cart.click_checkout_btn()
        self.cart.click_register_login_btn()
        self.login.fill_login_email(Data.login_email)
        self.login.fill_password(Data.password)
        self.login.click_login_btn()
        self.main.click_cart_btn()
        self.cart.check_product_is_in_cart(1)
        take_screenshot(self.page, 'test_twentieth')

    def test_twenty_first(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_products_btn()
        self.products.view_product_information(1)
        self.product_details.check_write_review_is_visible()
        self.product_details.fill_name_field(Data.username)
        self.product_details.fill_email_field(Data.login_email)
        self.product_details.fill_review_field(Data.review)
        self.product_details.click_submit_btn()
        self.product_details.check_successful_msg_is_visible()
        take_screenshot(self.page, 'test_twenty_first')

    def test_twenty_second(self, test_setup):
        self.main.check_page_is_visible()
        self.main.scroll_to_recommended_items()
        self.main.add_to_cart_recommended_item()
        self.main.click_cart_btn()
        self.cart.check_products_are_exist()
        take_screenshot(self.page, 'test_twenty_second')

    def test_twenty_third(self, test_setup):
        self.main.check_page_is_visible()
        self.main.click_login_btn()
        self.login.fill_name(Data.username)
        self.login.fill_signup_email(Data.signup_email)
        self.login.click_sign_up_btn()
        self.signup.create_new_account(Data.Mr, Data.password, Data.day, Data.month, Data.year, Data.first_name,
                                       Data.last_name, Data.company, Data.address_1, Data.address_2, Data.country,
                                       Data.city, Data.state, Data.zipcode, Data.mobile_number)
        self.account_created.check_account_created_is_visible()
        self.account_created.click_continue_btn()
        self.main.check_logged_in_text_is_visible(Data.username)
        self.main.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.checkout.check_delivery_address_information(Data.first_name, Data.last_name, Data.company, Data.address_1,
                                                         Data.address_2, Data.city, Data.state, Data.zipcode,
                                                         Data.country, Data.mobile_number)
        self.checkout.check_billing_address_information(Data.first_name, Data.last_name, Data.company, Data.address_1,
                                                        Data.address_2, Data.city, Data.state, Data.zipcode,
                                                        Data.country, Data.mobile_number)
        self.main.delete_account()
        self.account_deleted.check_account_deleted_is_visible()
        self.account_deleted.click_continue_btn()
        take_screenshot(self.page, 'test_twenty_third')

    def test_twenty_fourth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.add_product_to_cart(1)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.cart.click_register_login_btn()
        self.login.fill_name(Data.username)
        self.login.fill_signup_email(Data.signup_email)
        self.login.click_sign_up_btn()
        self.signup.create_new_account(Data.Mr, Data.password, Data.day, Data.month, Data.year, Data.first_name,
                                       Data.last_name, Data.company, Data.address_1, Data.address_2, Data.country,
                                       Data.city, Data.state, Data.zipcode, Data.mobile_number)
        self.account_created.check_account_created_is_visible()
        self.account_created.click_continue_btn()
        self.main.check_logged_in_text_is_visible(Data.username)
        self.main.click_cart_btn()
        self.cart.click_checkout_btn()
        self.checkout.check_delivery_address_information(Data.first_name, Data.last_name, Data.company, Data.address_1,
                                                         Data.address_2, Data.city, Data.state, Data.zipcode,
                                                         Data.country, Data.mobile_number)
        self.checkout.check_billing_address_information(Data.first_name, Data.last_name, Data.company, Data.address_1,
                                                        Data.address_2, Data.city, Data.state, Data.zipcode,
                                                        Data.country, Data.mobile_number)
        self.checkout.review_order(1)
        self.checkout.add_comment(Data.comment)
        self.checkout.place_order()
        self.payment.add_card_information(Data.card_name, Data.card_number, Data.cvc, Data.expiry_month,
                                          Data.expiry_year)
        self.payment.click_pay_btn()
        self.payment.click_download_invoice_btn()
        self.payment.click_continue_btn()
        self.main.delete_account()
        self.account_deleted.check_account_deleted_is_visible()
        self.account_deleted.click_continue_btn()
        take_screenshot(self.page, 'test_twenty_fourth')

    def test_twenty_fifth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.scroll_to_footer()
        self.main.scroll_up_by_arrow()
        take_screenshot(self.page, 'test_twenty_fifth')

    def test_twenty_sixth(self, test_setup):
        self.main.check_page_is_visible()
        self.main.scroll_to_footer()
        self.main.scroll_up()
        take_screenshot(self.page, 'test_twenty_sixth')
