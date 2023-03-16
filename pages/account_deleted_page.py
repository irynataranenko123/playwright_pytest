from playwright.sync_api import Page, expect


class AccountDeleted:

    def __init__(self, page: Page):
        self.page = page
        self.__account_deleted_text = self.page.locator('[data-qa="account-deleted"]>b')
        self.__continue_btn = self.page.locator('[class="pull-right"]')

    def check_account_deleted_is_visible(self) -> None:
        self.__account_deleted_text.wait_for(state='visible')
        expect(self.__account_deleted_text).to_contain_text('Account Deleted!')

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()
