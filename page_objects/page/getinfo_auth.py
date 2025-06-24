from page_objects.base_page import BasePage
from core.utils.files_helpers.help import *


class Locators:
    INPUT_PASSWORD = '//input[@id="sdo-password"]'
    INPUT_LOG_EMAIL_AUTH = '//input[@id="sdo-login"]'
    INPUT_LOG_EMAIL_RECOVER = '//div/input'
    EYE_PASSWORD = '//div[@class="eye-container"]'
    LOGO = '//div[@class="logo-auth mb-4"]'
    BUTTON_LOGIN = "//button/span[text()='Войти']"
    BUTTON_CANCEL = "//button/span[text()='Отмена']"
    BUTTON_RECOVER = "//button/span[text()='Восстановить']"
    LINK_FORGOT_PASSWORD = "//span[text()='Забыли пароль?']"
    NOTIFICATION_EMPTY_INPUTS = "//div[contains(@id, 'notification_')]//p[text()='Необходимо заполнить данные']"
    NOTIFICATION_INVALID_INPUTS = "//div[contains(@id, 'notification_')]//p[text()='Bad credentials.']"
    NOTIFICATION_INVALID_PASSWORD = "//div[contains(@id, 'notification_')]//p[text()='Введенный пароль недействителен.']"
    NOTIFICATION_VALID_FORGOT_PASSWORD = "//div[contains(@id, 'notification_')]//p[text()='Ссылка на изменение пароля отправлена на почту']"
    NOTIFICATION_INVALID_FORGOT_PASSWORD = "//div[contains(@id, 'notification_')]//p[text()='Пользователь не найден.']"
    HEADING_MY_COURSES = '//h3[text()="Мои курсы"]'

class AuthPage(BasePage):
    def input_login_auth(self, login_mail):
        self.fill_text(Locators.INPUT_LOG_EMAIL_AUTH, login_mail)

    def input_login_recover(self, login_mail):
        self.fill_text(Locators.INPUT_LOG_EMAIL_RECOVER, login_mail)

    def input_password(self, password):
        self.fill_text(Locators.INPUT_PASSWORD, password)

    def click_login(self):
        self.click(Locators.BUTTON_LOGIN)

    def click_forgot_password(self):
        self.click(Locators.LINK_FORGOT_PASSWORD)

    def click_hide_password(self):
        self.click(Locators.EYE_PASSWORD)

    def expect_visible_logo(self):
        self.expect_visible_elements(Locators.LOGO)

    def expect_hide_password(self):
        type_element = self.get_attribute_element(Locators.INPUT_PASSWORD, 'type')
        assert type_element == 'password'

    def expect_visible_password(self):
        type_element = self.get_attribute_element(Locators.INPUT_PASSWORD, 'type')
        assert type_element == 'text'

    def expect_notification(self, cred):
        if cred in (cred_empty_data, cred_empty_password):
            self.wait_visible_elements(Locators.NOTIFICATION_EMPTY_INPUTS)
        elif cred == cred_invalid_data:
            self.wait_visible_elements(Locators.NOTIFICATION_INVALID_INPUTS)
        elif cred == cred_invalid_password:
            self.wait_visible_elements(Locators.NOTIFICATION_INVALID_PASSWORD)

    def assert_valid_login(self):
        self.wait_visible_elements(Locators.HEADING_MY_COURSES)

    def expect_notification_recover_password(self, email):
        if email == cred_valid_data[0]:
            self.wait_visible_elements(Locators.NOTIFICATION_VALID_FORGOT_PASSWORD)
        if email == cred_invalid_data[0]:
            self.wait_visible_elements(Locators.NOTIFICATION_INVALID_FORGOT_PASSWORD)


    def click_recover_password(self):
        self.click(Locators.BUTTON_RECOVER)

    def click_cancel(self):
        self.click(Locators.BUTTON_RECOVER)
