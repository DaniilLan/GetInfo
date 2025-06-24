from core.utils.api_client import get_token
from page_objects.page.getinfo_auth import SerbPage
from playwright.sync_api import sync_playwright

import pytest


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
def auth(main_page):
    main_page.goto('https://dev2.getinfo.radugi.net')
    token = get_token()
    main_page.evaluate(
        """([token_key, token_value]) => {
            localStorage.setItem(token_key, token_value);
        }""",
        ["access", token]
    )
    main_page.reload()
    yield SerbPage(main_page)
