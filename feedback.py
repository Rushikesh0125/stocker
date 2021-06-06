from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class Feedback(Screen):
    def select(self, number):
        if number == 1:
            self.strng.get_screen('fb').ids.star1.opacity = 1
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "I Just Hate It!"
        elif number == 2:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 1
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "I Don't Like It!"
        elif number == 3:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 1
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "It is Good!"
        elif number == 4:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 1
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "It is Awesome!"
        elif number == 5:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 1
            self.strng.get_screen('fb').ids.text.text = "I Just Love It!"

    def feedback(self):
        cancel_btn_username_dialogue = MDFlatButton(text='OK', on_release=self.close_username_dialogue)
        self.dialog = MDDialog(title='Done', text='Feedback submitted', size_hint=(0.7, 0.2),
                               buttons=[cancel_btn_username_dialogue])
        self.dialog.open()
