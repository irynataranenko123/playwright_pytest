from playwright.sync_api import Page, expect
from definitions import ROOT_DIR


class ContactUs:

    def __init__(self, page: Page):
        self.page = page
        self.__get_in_touch_text = self.page.locator('[class="contact-form"]>h2')
        self.__name_field = self.page.locator('[data-qa="name"]')
        self.__email_field = self.page.locator('[data-qa="email"]')
        self.__subject_field = self.page.locator('[data-qa="subject"]')
        self.__message_field = self.page.locator('[data-qa="message"]')
        self.__upload_file_btn = self.page.locator('[name="upload_file"]')
        self.__submit_btn = self.page.locator('[name="submit"]')
        self.__successful_msg = self.page.locator('[class="status alert alert-success"]')
        self.__path = f'{ROOT_DIR}/utils/Files/pizza-cat.jpg'

    def check_get_in_touch_is_visible(self) -> None:
        self.__get_in_touch_text.wait_for(state='visible')
        expect(self.__get_in_touch_text).to_contain_text('Get In Touch')

    def fill_name(self, name) -> None:
        self.__name_field.type(name)

    def fill_email(self, email) -> None:
        self.__email_field.type(email)

    def fill_subject(self, subject) -> None:
        self.__subject_field.type(subject)

    def fill_message(self, message) -> None:
        self.__message_field.type(message)

    def click_submit_btn(self) -> None:
        self.__submit_btn.click()
        self.page.on("dialog", lambda dialog: dialog.accept())

    def check_successful_msg_is_visible(self) -> None:
        self.__successful_msg.wait_for(state='visible')
        expect(self.__successful_msg).to_contain_text('Success! Your details have been submitted successfully.')

    def upload_file(self) -> None:
        path = self.__path
        self.__upload_file_btn.set_input_files(path)
