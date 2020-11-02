from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from commons import web
from PO.Invitation_popup import InvitationPopup
import time


def before_all(context):
    context.browser = webdriver.Chrome()
    context.wait = WebDriverWait(context.browser, web.selenium_explicit_wait)
    context.browser.implicitly_wait(web.selenium_implicit_wait)
    web.context = context
    context.browser.maximize_window()
    context.browser.get(web.site_url)
    InvitationPopup.close_invitation_popup()


def after_all(context):
    context.browser.quit()


def after_step(context, step):
    time.sleep(context.config.userdata.getint("execution_delay"))



