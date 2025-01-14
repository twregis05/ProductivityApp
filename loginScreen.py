import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

# Import window screens
from homepage import Homepage
from leaderboardpage import Leaderboard
from calendarpage import Calendar
from suggestionpage import Suggestion
from accountpage import Account



class MyApp(App):
    def build(self):
        # Create ScreenManager to manage different screens
        sm = ScreenManager()

        # Add window screens
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(Homepage(name="homepage"))
        sm.add_widget(Leaderboard(name="leaderboard"))
        sm.add_widget(Calendar(name="calendar"))
        sm.add_widget(Account(name="account"))
        sm.add_widget(Suggestion(name="suggestion"))
        
        return sm

if __name__ == "__main__":
    MyApp().run()