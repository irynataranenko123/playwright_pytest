from playwright.sync_api import Page, expect
import re
from definitions import ROOT_DIR


class Payment:

    def __init__(self, page: Page):
        self.page = page
        self.__card_name_field = self.page.locator('[name="name_on_card"]')
        self.__card_number_field = self.page.locator('[name="card_number"]')
        self.__cvc_field = self.page.locator('[name="cvc"]')
        self.__expiry_month_field = self.page.locator('[name="expiry_month"]')
        self.__expiry_year_field = self.page.locator('[name="expiry_year"]')
        self.__pay_btn = self.page.locator('[id="submit"]')
        self.__successful_msg = self.page.locator('[data-qa="order-placed"]>b')
        self.__download_invoice_btn = self.page.locator('[class="btn btn-default check_out"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')
        self.__path = f'{ROOT_DIR}/utils/Files/invoice.txt'

    def add_card_information(self, name, number, cvc, month, year) -> None:
        self.__card_name_field.type(name)
        self.__card_number_field.type(number)
        self.__cvc_field.type(cvc)
        self.__expiry_month_field.type(month)
        self.__expiry_year_field.type(year)

    def fill_card_name(self, name) -> None:
        self.__card_name_field.type(name)

    def fill_card_number(self, number) -> None:
        self.__card_number_field.type(number)

    def fill_cvc(self, cvc) -> None:
        self.__cvc_field.type(cvc)

    def fill_expiry_month(self, month) -> None:
        self.__expiry_month_field.type(month)

    def fill_expiry_year(self, year) -> None:
        self.__expiry_year_field.type(year)

    def click_pay_btn(self) -> None:
        self.__pay_btn.click()

    def check_successful_msg_is_visible(self) -> None:
        self.__successful_msg.wait_for(state='visible')
        expect(self.__successful_msg).to_contain_text('Order Placed!')
        expect(self.page).to_have_url(re.compile(r'https://automationexercise.com/payment_done/*'))

    def click_download_invoice_btn(self) -> None:
        path = self.__path
        with self.page.expect_download() as download_info:
            self.__download_invoice_btn.click()
        download = download_info.value
        download.save_as(path)

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()
