from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def username_changer(self):
        self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {self.store.get('UserInfo')['name']}"
        self.strng.get_screen('pro').ids.uname.text = f"Welcome {self.store.get('UserInfo')['name']}"

    pass