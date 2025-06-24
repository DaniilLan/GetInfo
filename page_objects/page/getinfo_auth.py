from page_objects.base_page import BasePage


class Locators:
    INPUT_LOGIN = '//input[@id="sdo-login"]'
    INPUT_PASSWORD = '//input[@id="sdo-password"]'
    INPUT_LOG_EMAIL = '//div[@class="user-box"]/input'
    EYE_PASSWORD = '//div[@class="eye-container"]'
    LOGO = '//div[@class="logo-auth mb-4"]'
    BUTTON_LOGIN = "//button/span[text()='Войти']"
    BUTTON_CANCEL = "//button/span[text()='Отмена']"
    BUTTON_RECOVER = "//button/span[text()='Восстановить']"
    LINK_FORGOT_PASSWORD = "//span[text()='Забыли пароль?']"


class AuthPage(BasePage):
    def input_login(self, login):
        self.fill_text(Locators.INPUT_LOGIN, login)

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

    def expect_visible_notification(self):
        t