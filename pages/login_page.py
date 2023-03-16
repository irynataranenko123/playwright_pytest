from playwright.sync_api import Page, expect


class Login:

    def __init__(self, page: Page):

        self.page = page
        self.__new_user_text = self.page.locator('[class="signup-form"]>h2')
        self.__name_field = self.page.locator('[name="name"]')
        self.__signup_email_field = self.page.locator('[data-qa="signup-email"]')
        self.__sign_up_btn = self.page.locator('[data-qa="signup-button"]')
        self.__login_to_account_text = self.page.locator('[class="login-form"]>h2')
        self.__login_email_field = self.page.locator('[data-qa="login-email"]')
        self.__password_field = self.page.locator('[data-qa="login-password"]')
        self.__login_btn = self.page.locator('[data-qa="login-button"]')
        self.__error_invalid_data_msg = self.page.locator('[action = "/login"]>p')
        self.__error_email_exist_msg = self.page.locator('[action = "/signup"]>p')

    def check_new_user_is_visible(self) -> None:
        self.__new_user_text.wait_for(state='visible')
        expect(self.__new_user_text).to_contain_text('New User Signup!')

    def fill_name(self, username) -> None:
        self.__name_field.type(username)

    def fill_signup_email(self, email) -> None:
        self.__signup_email_field.type(email)

    def click_sign_up_btn(self) -> None:
        self.__sign_up_btn.click()

    def check_login_to_account_is_visible(self) -> None:
        self.__login_to_account_text.wait_for(state='visible')
        expect(self.__login_to_account_text).to_contain_text('Login to your account')

    def fill_login_email(self, email) -> None:
        self.__login_email_field.type(email)

    def fill_password(self, password) -> None:
        self.__password_field.type(password)

    def click_login_btn(self) -> None:
        self.__login_btn.click()

    def check_error_invalid_data_msg_is_visible(self) -> None:
        self.__error_invalid_data_msg.wait_for(state='visible')
        expect(self.__error_invalid_data_msg).to_contain_text('Your email or password is incorrect!')

    def check_error_email_exist_msg_is_visible(self) -> None:
        self.__error_email_exist_msg.wait_for(state='visible')
        expect(self.__error_email_exist_msg).to_contain_text('Email Address already exist!')
