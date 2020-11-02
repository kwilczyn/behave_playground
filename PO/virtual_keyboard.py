from commons import web


class VirtualKeyboard:

    virtual_keyboard_popup = "//div[@id='kbd']"
    shift_button = "//button[@id='K16']"
    ctrl_alt_button = "//button[@id='K273']"
    space_button = "//button[@id='K32']"

    @classmethod
    def _get_button_selector(cls, char):
        char = str(char)
        if len(char) > 1:
            raise ValueError("Only one char should be provided!")
        if char == " ":
            return cls.space_button
        return f"{cls.virtual_keyboard_popup}//button[contains(.,'{char}')]"

    @classmethod
    def click_key_button(cls, char):
        if char.isupper() or not char.isalnum():
            cls.click_shift()
        key_button_selector = cls._get_button_selector(char)
        web.click_element(key_button_selector)

    @classmethod
    def click_shift(cls):
        web.click_element(cls.shift_button)

    @classmethod
    def click_ctrl_alt(cls):
        web.click_element(cls.ctrl_alt_button)

    @classmethod
    def type_string(cls, string_value):
        """
        This method doesn't support unicode characters.
        If you need to write some national characters use _click_ctrl_alt and click_key_button instead
        """
        for char in str(string_value):
            cls.click_key_button(char)
