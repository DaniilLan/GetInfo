import time

from page_objects.base_page import BasePage
from core.utils.files_helpers.help import *


class Locators:
    SECTION_EDUCATION_CENTER = '//li[@data-cy="submenu-ms-education-center"]/div[span[text()="Учебный центр"]]'
    SUBSECTION_COMPANIES = '//li[@class="el-menu-item"][.//a[text()="Компания"]]'
    LINK_HEAD_NAME = '//div[@class="description-value"]/a[@target="_blank"]'
    EMAIL_USER = '//div[@class="font-bold text-center"]'
    LINK_EMAIL_USER = '//div[@class="text-center"]/a[@target="_blank"]'
    NAME_HEAD = '(//div[@class="description-value"])[2]'
    NAME_USER = '//div[@class="font-bold text-center"]'

class UserPage(BasePage):

    def login(self):
        self.fill_text('//input[@id="sdo-login"]', cred_valid_data[0])
        time.sleep(2)
        self.fill_text('//input[@id="sdo-password"]', cred_valid_data[1])
        self.click("//button/span[text()='Войти']")

    def click_education_center(self):
        self.click(Locators.SECTION_EDUCATION_CENTER)

    def click_companies(self):
        self.click(Locators.SUBSECTION_COMPANIES)

    def click_name_head(self):
        self.click(Locators.LINK_HEAD_NAME)

    def assert_link_name_user_and_head(self):
        link_head = self.get_attribute_element(Locators.LINK_HEAD_NAME, 'href')
        link_user = self.get_attribute_element(Locators.LINK_EMAIL_USER, 'href')
        assert link_user == link_head, f'Ошибка сравнения {link_user} and {link_head}'

    def assert_text_name_user_and_head(self):
        text_head = self.get_text(Locators.LINK_HEAD_NAME)
        text_user = self.get_text(Locators.NAME_USER)
        assert text_user == text_head, f'Ошибка сравнения {text_user} and {text_head}'
