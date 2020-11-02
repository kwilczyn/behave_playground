from commons import web
from selenium.webdriver.common.keys import Keys


class MainPage:

    search_button = "//input[@name='btnK']"
    search_inputbox = "//input[@name='q']"
    main_page_iframe = "//iframe[@id='backgroudImage']"
    virtual_keyboard_button = "//img[@tia_field_name='q']/../../span"

    @classmethod
    def click_search_button(cls):
        web.click_element(cls.search_button)

    @classmethod
    def set_search_inputbox(cls, value):
        web.set_inputbox(cls.search_inputbox, value)

    @classmethod
    def confirm_serching(cls):
        cls.set_search_inputbox(Keys.RETURN)

    @classmethod
    def search_for_value(cls, value):
        cls.set_search_inputbox(value)
        cls.confirm_serching()

    @classmethod
    def get_current_search_inputbox_value(cls):
        return web.get_current_value_from_inputbox(cls.search_inputbox)

    @classmethod
    def click_virtual_keyboard_button(cls):
        web.click_element(cls.virtual_keyboard_button)

