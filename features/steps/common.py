from behave import *
from PO.Invitation_popup import InvitationPopup
from commons import web


@given("Browser is open on google main site")
def step_imp(context):
    context.browser.get(web.site_url)


@given("that invitation popup is closed")
def step_imp(context):
    InvitationPopup.close_invitation_popup()
