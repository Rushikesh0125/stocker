from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from sqlite3 import *
from kivymd.uix.list import TwoLineListItem
import requests
from bs4 import BeautifulSoup
from kivymd.utils import asynckivy
from kivymd.uix.list import IRightBodyTouch, IconRightWidget, ThreeLineAvatarIconListItem, ThreeLineListItem, TwoLineAvatarIconListItem, TwoLineListItem


class Nav(Screen):

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('1s').manager.current = '1s'
        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'

    def showstock(self):
        con = connect('stocker.db')
        cursor = con.cursor()
        sql = "select company_name,investment_price from stockinfo"
        data = cursor.execute(sql).fetchall()
        for d in data:
            result = str(d[0])
            result1 = str(d[1])
            con.commit()
            item = TwoLineListItem()
            item.text = result
            a9 = result
            url = "https://www.google.com/finance/quote/" + a9 + ":NSE"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': 'rPF6Lc'})[0].find('span').text
            item.secondary_text = "current price: " + price
            item.tertiary_text = "Initial investment price: " + result1
            self.strng.get_screen("1s").ids["dock"].add_widget(item)

    def showstock1(self):
        global result
        con = connect('stocker.db')
        cursor = con.cursor()
        sql = "select company_name,investment_price from stockinfo"
        data = cursor.execute(sql).fetchall()
        for d in data:
            result = str(d[0])
            result1 = str(d[1])
        con.commit()
        item = ThreeLineListItem()
        item.text = result
        a9 = result
        url = "https://www.google.com/finance/quote/" + a9 + ":NSE"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find_all('div', {'class': 'rPF6Lc'})[0].find('span').text
        item.secondary_text = "current price: " + price
        item.tertiary_text = "Initial investment price: " + result1
        self.strng.get_screen("1s").ids["dock"].add_widget(item)

    def cv(self):
        sum = 0
        con = connect('stocker.db')
        cursor = con.cursor()
        sql = "select (investment_price * quantity) from stockinfo where (investment_price * quantity)>0"
        res = cursor.execute(sql).fetchall()
        for i in res:
            sum = sum + float(i[0])
        total =  "  Net worth\n" + str(sum)
        return total

    def updatecv(self,dt):
        self.strng.get_screen('1s').ids.ooo.text = self.cv()


    def priceTracker(a):
        url = "https://www.google.com/finance/quote/SENSEX:INDEXBOM"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # name = soup.find_all('div', {'class': 'Fz(xs) Fw(b) C($negativeColor)'})[0].find('span').text
        price = soup.find_all('div', {'class': 'rPF6Lc'})[0].find('span').text
        return ("   Sensex \n" + price)

    def priceTracker1(a):
        url = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find_all('div', {'class': 'rPF6Lc'})[0].find('span').text
        return ("  Nifty \n" + price)

    def set_heading1(self, dt):
        async def set_heading1():
            await asynckivy.sleep(0.1)
            text_heading = self.strng.get_screen('1s').ids.sss
            text_heading.text = self.priceTracker1()
            text_heading = self.strng.get_screen('1s').ids.rrr
            text_heading.text = self.priceTracker()
            self.strng.get_screen('1s').ids.ooo.text = self.cv()

        asynckivy.start(set_heading1())
    pass