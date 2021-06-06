from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class UsernameScreen(Screen):
    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        self.password_text = self.strng.get_screen('usernamescreen').ids.pw_text.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == [] and self.password_text.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Enter Username And password',
                                   text="Please input  username and password for registration", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    pass