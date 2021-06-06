from sqlite3 import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class Add(Screen):
    def savestock(self):
        a = self.strng.get_screen('add').ids.company.text
        b = float(self.strng.get_screen('add').ids.invest.text)
        c = self.strng.get_screen('add').ids.quantity.text
        if a.split() == [] or b == [] or c.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text="Please fill the required fields", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif a.isalnum() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text="Please enter valid company name", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif c.isnumeric() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text="Please enter valid price", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            try:
                con = connect('stocker.db')
                cursor = con.cursor()
                sql = "insert into stockinfo values('%s','%s','%s')"
                cursor.execute(sql % (a,b,c))
                con.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Ok', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Saved', text="Stock Added", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
                con.close()
            except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Issue', text="Some Error occured", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

    pass