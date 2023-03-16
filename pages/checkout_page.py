from playwright.sync_api import Page, expect


class Checkout:

    def __init__(self, page: Page):

        self.page = page
        self.__checkout_details = self.page.locator('[class="checkout-information"]')
        self.__firs_name_last_name = self.page.locator('[class="address item box"]>li:nth-child(2)')
        self.__company = self.page.locator('[class="address item box"]>li:nth-child(3)')
        self.__address_1 = self.page.locator('[class="address item box"]>li:nth-child(4)')
        self.__address_2 = self.page.locator('[class="address item box"]>li:nth-child(5)')
        self.__city_state_postcode = self.page.locator('[class="address item box"]>li:nth-child(6)')
        self.__country = self.page.locator('[class="address item box"]>li:nth-child(7)')
        self.__phone = self.page.locator('[class="address item box"]>li:nth-child(8)')
        self.__firs_name_last_name_billing = self.page.locator('[class="address alternate_item box"]>li:nth-child(2)')
        self.__company_billing = self.page.locator('[class="address alternate_item box"]>li:nth-child(3)')
        self.__address_1_billing = self.page.locator('[class="address alternate_item box"]>li:nth-child(4)')
        self.__address_2_billind = self.page.locator('[class="address alternate_item box"]>li:nth-child(5)')
        self.__city_state_postcode_billing = self.page.locator('[class="address alternate_item box"]>li:nth-child(6)')
        self.__country_billing = self.page.locator('[class="address alternate_item box"]>li:nth-child(7)')
        self.__phone_billing = self.page.locator('[class="address alternate_item box"]>li:nth-child(8)')
        self.__product = self.page.locator('tbody>tr:first-child')
        self.__text_field = self.page.locator('[class="form-control"]')
        self.__place_order_btn = self.page.locator('[href="/payment"]')


    def check_address_details_is_visible(self) -> None:
        self.__checkout_details.wait_for(state='visible')

    def check_delivery_address_information(self, first_name, last_name, company, address1, address2, city, state, postcode,
                                  country, phone) -> None:
        expect(self.__firs_name_last_name).to_contain_text(first_name)
        expect(self.__firs_name_last_name).to_contain_text(last_name)
        expect(self.__company).to_contain_text(company)
        expect(self.__address_1).to_contain_text(address1)
        expect(self.__address_2).to_contain_text(address2)
        expect(self.__city_state_postcode).to_contain_text(city)
        expect(self.__city_state_postcode).to_contain_text(state)
        expect(self.__city_state_postcode).to_contain_text(postcode)
        expect(self.__country).to_contain_text(country)
        expect(self.__phone).to_contain_text(phone)

    def review_order(self, number) -> None:
        self.__product.wait_for(state='visible')
        expect(self.__product).to_have_attribute('id', f'product-{number}')

    def add_comment(self, text) -> None:
        self.__text_field.type(text)

    def place_order(self) -> None:
        self.__place_order_btn.click()

    def check_billing_address_information(self, first_name, last_name, company, address1, address2, city, state,
                                          postcode, country, phone):
        expect(self.__firs_name_last_name_billing).to_contain_text(first_name)
        expect(self.__firs_name_last_name_billing).to_contain_text(last_name)
        expect(self.__company_billing).to_contain_text(company)
        expect(self.__address_1_billing).to_contain_text(address1)
        expect(self.__address_2_billind).to_contain_text(address2)
        expect(self.__city_state_postcode_billing).to_contain_text(city)
        expect(self.__city_state_postcode_billing).to_contain_text(state)
        expect(self.__city_state_postcode_billing).to_contain_text(postcode)
        expect(self.__country_billing).to_contain_text(country)
        expect(self.__phone_billing).to_contain_text(phone)