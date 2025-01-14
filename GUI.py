import kivy
import sqlite3
from loginscreen import LoginScreen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class MainAppScreen(Screen):
    pass

class AppScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)

class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(LoginScreen(name="login"))
        manager.add_widget(MainAppScreen(name="main"))
        return manager

if __name__ == "__main__":
    MyApp().run()


