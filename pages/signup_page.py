from playwright.sync_api import Page, expect


class SignUp:

    def __init__(self, page: Page):
        self.page = page
        self.__enter_information_text = self.page.locator('[class ="login-form"]>h2:first-child')
        self.__input_password = self.page.locator('[id="password"]')
        self.__day_of_birth_dropdown = self.page.locator('[id="days"]')
        self.__month_of_birth_dropdown = self.page.locator('[id="months"]')
        self.__year_of_birth_dropdown = self.page.locator('[id="years"]')
        self.__newsletter_checkbox = self.page.locator('[id="newsletter"]')
        self.__special_offers_checkbox = self.page.locator('[id="optin"]')
        self.__input_first_name = self.page.locator('[id="first_name"]')
        self.__input_last_name = self.page.locator('[id="last_name"]')
        self.__input_company = self.page.locator('[id="company"]')
        self.__input_address_1 = self.page.locator('[id="address1"]')
        self.__input_address_2 = self.page.locator('[id="address2"]')
        self.__country_dropdown_list = self.page.locator('[id="country"]')
        self.__input_state = self.page.locator('[id="state"]')
        self.__input_city = self.page.locator('[id="city"]')
        self.__input_zipcode = self.page.locator('[id="zipcode"]')
        self.__input_mobile_number = self.page.locator('[id="mobile_number"]')
        self.__create_account_btn = self.page.locator('[data-qa="create-account"]')

    def check_enter_information_is_visible(self) -> None:
        self.__enter_information_text.wait_for(state='visible')
        expect(self.__enter_information_text).to_contain_text('Enter Account Information')

    def fill_password(self, password):
        self.__input_password.type(password)

    def create_new_account(self, name, password, day, month, year, first_name, last_name, company, address_1, address_2, country,
                           state, city, zipcode, mobile_number):
        radio_btn = self.page.locator(f'[id="uniform-id_{name}"]')
        radio_btn.check(force=True)
        self.__input_password.type(password)
        self.__day_of_birth_dropdown.select_option(day)
        self.__month_of_birth_dropdown.select_option(month)
        self.__year_of_birth_dropdown.select_option(year)
        self.__newsletter_checkbox.check()
        self.__special_offers_checkbox.check()
        self.__input_first_name.type(first_name)
        self.__input_last_name.type(last_name)
        self.__input_company.type(company)
        self.__input_address_1.type(address_1)
        self.__input_address_2.type(address_2)
        self.__country_dropdown_list.select_option(country)
        self.__input_state.type(state)
        self.__input_city.type(city)
        self.__input_zipcode.type(zipcode)
        self.__input_mobile_number.type(mobile_number)
        self.__create_account_btn.click()

    def select_radio_btn(self, name) -> None:
        radio_btn = self.page.locator(f'[id="uniform-id_{name}"]')
        radio_btn.check(force=True)

    def select_day(self, day) -> None:
        self.__day_of_birth_dropdown.select_option(day)

    def select_month(self, month) -> None:
        self.__month_of_birth_dropdown.select_option(month)

    def select_year(self, year) -> None:
        self.__year_of_birth_dropdown.select_option(year)

    def check_newsletter_checkbox(self) -> None:
        self.__newsletter_checkbox.check()

    def check_special_offers_checkbox(self) -> None:
        self.__special_offers_checkbox.check()

    def fill_first_name(self, first_name) -> None:
        self.__input_first_name.type(first_name)

    def fill_last_name(self, last_name) -> None:
        self.__input_last_name.type(last_name)

    def fill_company(self, company) -> None:
        self.__input_company.type(company)

    def fill_address_1(self, address_1) -> None:
        self.__input_address_1.type(address_1)

    def fill_address_2(self, address_2) -> None:
        self.__input_address_2.type(address_2)

    def select_country(self, country) -> None:
        self.__country_dropdown_list.select_option(country)

    def fill_state(self, state) -> None:
        self.__input_state.type(state)

    def fill_city(self, city) -> None:
        self.__input_city.type(city)

    def fill_zipcode(self, zipcode) -> None:
        self.__input_zipcode.type(zipcode)

    def fill_mobile_number(self, mobile_number) -> None:
        self.__input_mobile_number.type(mobile_number)

    def click_create_account_btn(self) -> None:
        self.__create_account_btn.click()