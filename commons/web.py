from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

global context
selenium_implicit_wait = 10
selenium_explicit_wait = 5
site_url = "http://google.com"


def wait_until_element_is_visible(xpath):
    context.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))


def find_element(xpath):
    return context.browser.find_element_by_xpath(xpath)


def find_elements(xpath):
    return context.browser.find_elements_by_xpath(xpath)


def click_element(xpath):
    wait_until_element_is_visible(xpath)
    element = find_element(xpath)
    element.click()


def switch_to_iframe(xpath):
    wait_until_element_is_visible(xpath)
    iframe = find_element(xpath)
    context.browser.switch_to_frame(iframe)


def set_inputbox(xpath, value):
    wait_until_element_is_visible(xpath)
    inputbox = find_element(xpath)
    inputbox.send_keys(value)


def get_attribute_value_from_element(xpath, attribute):
    wait_until_element_is_visible(xpath)
    inputbox = find_element(xpath)
    return inputbox.get_attribute(attribute)


def get_current_value_from_inputbox(xpath):
    return get_attribute_value_from_element(xpath, "value")
