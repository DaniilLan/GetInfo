import time

import pytest


class TestAuth:

    # Пример 1 (сравнение ссылок)
    def test_access1_info_companies(self, page_user):
        page_user.login()
        page_user.click_education_center()
        page_user.click_companies()
        page_user.assert_link_name_user_and_head()

    # Пример 2 (сравнение текста элементов)
    def test_access2_info_companies(self, page_user):
        page_user.login()
        page_user.click_education_center()
        page_user.click_companies()
        page_user.click_name_head()
        time.sleep(2)
        page_user.assert_text_name_user_and_head()

