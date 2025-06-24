from core.utils.files_helpers.help import *

import pytest


class TestAuth:

    def test_login_valid(self, page_auth):
        page_auth.input_login_auth(cred_valid_data[0])
        page_auth.input_password(cred_valid_data[1])
        page_auth.click_login()
        page_auth.assert_valid_login()

    @pytest.mark.parametrize(
        'cred', [
            cred_empty_data,
            cred_invalid_data,
            cred_empty_password,
            cred_invalid_password,
        ],
        ids=[
            'Пустые поля ввода',
            'Неверные данные',
            'Пустое поле пароль',
            'Неверный пароль',
        ]
    )
    def test_login_invalid_cred(self, page_auth, cred):
        page_auth.input_login_auth(cred[0])
        page_auth.input_password(cred[1])
        page_auth.click_login()
        page_auth.expect_notification(cred)

    def test_hide_and_visible_password(self, page_auth):
        page_auth.input_password(cred_invalid_password[1])
        page_auth.click_hide_password()
        page_auth.expect_visible_password()
        page_auth.click_hide_password()
        page_auth.expect_hide_password()

    @pytest.mark.parametrize(
        'email', [
            cred_valid_data[0],
            cred_invalid_data[0],
        ],
        ids=[
            'Валидные почта,',
            'Несуществующая почта',
        ]
    )
    def test_recover_password(self, page_auth, email):
        page_auth.click_forgot_password()
        page_auth.input_login_recover(email)
        page_auth.click_recover_password()
        page_auth.expect_notification_recover_password(email)







