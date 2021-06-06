from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.list import IRightBodyTouch, IconRightWidget, TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from stringz import KV
from kivymd.uix.picker import MDDatePicker
from Navs import Nav
from Add import *
from edit import *
from password import *
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
import importlib

Window.size = (400, 500)

class Profile(Screen):
    pass
class setting(Screen):
    pass
class WelcomeScreen(Screen):
    pass
class contactus(Screen):
    pass
class Feedback(Screen):
    pass
class UsernameScreen(Screen):
    pass
class DOB(Screen):
    pass
class MainScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Nav(name='1s'))
sm.add_widget(Add(name='add'))
sm.add_widget(Profile(name='pro'))
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(UsernameScreen(name='usernamescreen'))
sm.add_widget(DOB(name='dob'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(setting(name='s'))
sm.add_widget(Password(name='password'))
sm.add_widget(contactus(name='cu'))
sm.add_widget(Feedback(name='fb'))

class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class Stoker(MDApp,Nav,Add,Profile,WelcomeScreen,UsernameScreen,DOB,MainScreen,setting,Password,Feedback):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Light'
        self.strng = Builder.load_string(KV)


    def build(self):
        con = connect('stocker.db')
        cursor = con.cursor()
        res = cursor.execute("select * from profileinfo").fetchall()
        for d in res:
            name = d[0]
            email = d[1]
            phone = d[2]
        name = self.strng.get_screen('pro').ids.uname.text
        email = self.strng.get_screen('pro').ids.uemail.text
        phone = self.strng.get_screen('pro').ids.uphone.text
        self.showstock()
        return self.strng

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('1s').manager.current = '1s'
        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'

    def username_changer(self):
        self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {self.store.get('UserInfo')['name']}"
        self.strng.get_screen('pro').ids.uname.text = f"Welcome {self.store.get('UserInfo')['name']}"

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date, year=1999, month=1, day=1, )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        self.strng.get_screen('dob').ids.date_picker.text = str(self.dob)
        self.strng.get_screen('dob').ids.second_disabled.disabled = False

        # Storing of DATA
        self.store.put('UserInfo', name=self.username_text, password=self.password_text, dob=str(self.dob))
        self.username_changer()

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

    def close_username_dialogue(self, obj):
        self.dialog.dismiss()

    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    Stoker().run()