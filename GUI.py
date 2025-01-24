import kivy
import sqlite3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from homepage import Homepage
from leaderboardpage import Leaderboard
from calendarpage import Calendar
from suggestionpage import Suggestion
from accountpage import Account
from loginscreen import LoginScreen

class MainAppScreen(Screen):
    def __init__(self, **kwargs):
        super(MainAppScreen, self).__init__(**kwargs)
        
        grid = GridLayout(cols=1, rows=2)

        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(Homepage(name="homepage"))
        self.sm.add_widget(Leaderboard(name="leaderboard"))
        self.sm.add_widget(Calendar(name="calendar"))
        self.sm.add_widget(Suggestion(name="suggestion"))
        self.sm.add_widget(Account(name="account"))

        grid.add_widget(self.sm)

        buttonRow = GridLayout(cols=5, size_hint_y=0.2)
        
        calendarBut = Button(text="Calendar", font_size=16)
        leaderBut = Button(text="LeaderBoard", font_size=16)
        homepageBut = Button(text="HomePage", font_size=16)
        suggestionBut = Button(text="Suggestion", font_size=16)
        profileBut = Button(text="Account", font_size=16)
        buttonRow.add_widget(calendarBut)
        buttonRow.add_widget(leaderBut)
        buttonRow.add_widget(homepageBut)
        buttonRow.add_widget(suggestionBut)
        buttonRow.add_widget(profileBut)

        # Bind the buttons to their corresponding functions
        calendarBut.bind(on_press=self.on_calendar_click)
        leaderBut.bind(on_press=self.on_leaderboard_click)
        homepageBut.bind(on_press=self.on_homepage_click)
        suggestionBut.bind(on_press=self.on_suggestion_click)
        profileBut.bind(on_press=self.on_profile_click)

        grid.add_widget(buttonRow)

        self.add_widget(grid)
    
    def on_calendar_click(self, instance):
        self.sm.current = "calendar"

    def on_leaderboard_click(self, instance):
        self.sm.current = "leaderboard"

    def on_homepage_click(self, instance):
        self.sm.current = "homepage"

    def on_suggestion_click(self, instance):\
        self.sm.current = "suggestion"

    def on_profile_click(self, instance):
        self.sm.current = "account"

class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(LoginScreen(name="login"))
        manager.add_widget(MainAppScreen(name="main"))
        return manager

if __name__ == "__main__":
    MyApp().run()


