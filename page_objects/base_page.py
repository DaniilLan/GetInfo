from typing import Union, List
from playwright.sync_api import expect, Page

import urllib.parse


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri: str):
        """Открыть страницу"""
        self.page.goto(uri)
        self.page.wait_for_load_state()

    def get_url(self):
        """Получить URI"""
        return self.page.url

    def click(self, locator: str):
        """Кликнуть по элементу"""
        self.wait_visible_elements(locator)
        self.page.click(locator)

    def click_on_elements(self, locator: str):
        """Кликнуть по всем элементам, соответствующим локатору"""
        elements = self.page.locator(locator).all()
        for element in elements:
            expect(element).to_be_visible()
            element.click()

    def fill_text(self, locator: str, value: str):
        """Ввод текста в поле"""
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        element.fill(value)

    def get_text(self, locator: str):
        """Получить текст элемента"""
        self.page.is_visible(locator)
        return self.page.locator(locator).text_content()

    def expect_text(self, locator: str, text_element: str):
        """Проверка соответствия текста ОР"""
        element = self.page.locator(locator)
        return expect(element).to_have_text(text_element)

    def get_list_text(self, locator: str):
        """Получить объединенный текст всех элементов"""
        elements = self.page.locator(locator).all()
        text = "".join(element.text_content() for element in elements)
        if text is None:
            raise ValueError(f"У элемента с локатором = {locator}, отсутствует текст")
        return text

    def wait_visible_elements(self, locators: Union[str, List[str]], timeout_sec: int = 30):
        """Ожидать появления элемента(ов)"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            self.page.wait_for_selector(
                locator,
                state="visible",
                timeout=timeout_sec * 1000
            )

    def wait_after_appearance(self, locator):
        if self.expect_visible_elements(locator):
            self.wait_time(1000)

    def expect_not_visible_elements(self, locators: Union[str, List[str]]):
        """Проверка - элемент не виден"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            return expect(self.page.locator(locator)).not_to_be_visible()

    def expect_visible_elements(self, locators: Union[str, List[str]]):
        """Проверка - элементы видны"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            if self.page.is_visible(locator):
                return True
        return False

    def get_quantity_elements(self, locator: str):
        """Получить количество элементов"""
        elements = self.page.locator(locator).all()
        return len(elements)

    def get_attribute_element(self, locator: str, type_attribute: str):
        """Получить атрибуты элемента"""
        element = self.page.locator(locator)
        return element.get_attribute(type_attribute)

    def expect_style_element(self, locator, name_style: str, value_style: str):
        """Проверка - 'имя' и 'значение' стиля элемента равны заданным параметрам (name_style, value_style)"""
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_style, value_style)

    def clear_inputs(self, locators: Union[str, List[str]]):
        """Очистить поле ввода"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            self.page.locator(locator).clear()
            return expect(self.page.locator(locator)).to_be_empty()

    def expect_css_style(self, locator: str, name_css: str, param_css: str):
        """Проверка параметров стиля элемента"""
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_css, param_css)

    def hovering_on_element(self, locator: str):
        """Навестить курком на элемент."""
        self.wait_visible_elements(locator)
        self.page.hover(locator)

    def expect_url(self, url: str):
        """Ожидание конкретного URL на текущей странице"""
        self.page.wait_for_url(url)
        self.page.wait_for_load_state()

    def wait_load_state_networking(self):
        """Ожидание конкретного URL на текущей странице"""
        self.page.wait_for_load_state("networkidle")

    def expect_url_pdf(self, url_pdf: str, locator: str):
        """Ожидание открытого URL (PDF)"""
        with self.page.context.expect_page() as new_page_info:
            self.click(locator)
        new_page = new_page_info.value
        decoded_url = urllib.parse.unquote(new_page.url)
        assert decoded_url == url_pdf, (f"Страница файла не соответствует ожиданию"
                                        f"Текущая: {decoded_url}"
                                        f"Ожидаемая: {url_pdf}")

    def element_has_class(self, locator: str, expected_class: str):
        """Ожидание определенного класса у элемента - True/False"""
        self.page.wait_for_selector(locator, state="visible")
        class_attribute = self.page.get_attribute(locator, "class")
        return class_attribute is not None and expected_class in class_attribute.split()

    def wait_time(self, time: int):
        """Ожидание в миллисекундах"""
        self.page.wait_for_timeout(time)