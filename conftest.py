import json
import pytest

from page_objects.page.getinfo_user import UserPage
from page_objects.page.getinfo_auth import AuthPage
from playwright.sync_api import sync_playwright


@pytest.fixture()
def main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=100,
        )
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
        )
        page = context.new_page()
        yield page

@pytest.fixture()
def page_auth(main_page):
    main_page.goto('https://dev2.getinfo.radugi.net')
    yield AuthPage(main_page)

@pytest.fixture()
def page_user(main_page):
    main_page.goto('https://dev2.getinfo.radugi.net')
    yield UserPage(main_page)

# @pytest.fixture()
# def auth_user(main_page):
#     main_page.goto('https://dev2.getinfo.radugi.net')
#     token_data = get_token()
#     token_string = json.dumps({
#         "accessToken": token_data["accessToken"],
#         "refreshToken": token_data["refreshToken"]
#     })
#     full_token_string = f'auth-tokens-production {token_string}'
#     main_page.evaluate(
#         """([token_key, token_value]) => {
#             localStorage.setItem(token_key, token_value);
#         }""",
#         ["auth-tokens-production", full_token_string]
#     )
#     main_page.reload()
#     yield UserPage(main_page)
