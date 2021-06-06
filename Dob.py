from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker


class DOB(Screen):
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
    pass