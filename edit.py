from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from sqlite3 import *
from kivymd.uix.dialog import MDDialog


class Edit(Screen):
    def saveprofile(self):
        a = self.strng.get_screen('edit').ids.username.text
        b = self.strng.get_screen('edit').ids.email.text
        c = self.strng.get_screen('edit').ids.contact.text
        if a.split() == [] or b.split() == [] or c.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Please fill the required details', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif a.isalnum() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Enter valid username', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif c.isnumeric() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Enter valid mobile number', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            try:
                con = connect('stocker.db')
                cursor = con.cursor()
                sql = "insert into profileinfo values('%s','%s','%s')"
                cursor.execute(sql % (a, b, c))
                con.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Ok', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Saved', text="Profile Created Successfully", size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
                con.close()
            except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Issue', text="Some Error occured", size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

    pass