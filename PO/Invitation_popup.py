from commons import web


class InvitationPopup:

    invitation_popup_frame = "//div[@id='cnsw']/iframe"
    agree_button = "//div[@id='introAgreeButton']"
    show_more_button = "//div[@role='navigation']/div[@role='presentation']"

    @classmethod
    def switch_to_invitation_popup(cls):
        web.switch_to_iframe(cls.invitation_popup_frame)

    @classmethod
    def click_agree_button(cls):
        web.click_element(cls.agree_button)

    @classmethod
    def click_more_information_button(cls):
        web.click_element(cls.show_more_button)

    @classmethod
    def close_invitation_popup(cls):
        cls.switch_to_invitation_popup()
        cls.click_agree_button()
