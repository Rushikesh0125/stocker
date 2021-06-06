from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from sqlite3 import *


class Password(Screen):
    def changepass(self):
        a = self.strng.get_screen('password').ids.cur_pass.text
        b = self.strng.get_screen('password').ids.new_pass.text
        c = self.strng.get_screen('password').ids.con_pass.text
        if a.split() == [] or b.split() == [] or c.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Please fill the required details', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            if b == c:
                try:
                    con = connect('stocker.db')
                    cursor = con.cursor()
                    sql = "insert into changepass values('%s','%s','%s')"
                    cursor.execute(sql % (a, b, c))
                    con.commit()
                    cancel_btn_username_dialogue = MDFlatButton(text='Ok', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='Saved', text="Password Changed Successfully", size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
                    con.close()
                except Exception as e:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='Issue', text="Some Error occured", size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Issue', text='Password does not match', size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

    pass