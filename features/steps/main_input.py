from behave import *
from PO.main_page import MainPage
from PO.virtual_keyboard import VirtualKeyboard
import time


@when("User provides {number} long value on the main page")
def step_imp(context, number):
    value = "a"*int(number)
    MainPage.set_search_inputbox(value)


@then("Only maximum number of characters has been written")
def step_imp(context):
    assert len(MainPage.get_current_search_inputbox_value()) <= 2048


@when("User provides value using virtual keyboard")
def step_imp(context):
    MainPage.click_virtual_keyboard_button()
    context.text_to_check = "My ex!@mple VALUE 123"
    VirtualKeyboard.type_string(context.text_to_check)


@then("given value is enabled in the searchbox")
def step_imp(context):
    assert MainPage.get_current_search_inputbox_value() == context.text_to_check
