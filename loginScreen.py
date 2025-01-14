import kivy
from kivy.app import App
from kivy.uix.button import Button
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

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        user_label = Label(text="Username")
        layout.add_widget(user_label)
        self.username = TextInput(multiline=False)
        layout.add_widget(self.username)

        pass_label = Label(text="Password")
        layout.add_widget(pass_label)
        self.password = TextInput(multiline=False)
        layout.add_widget(self.password)

        submit_button = Button(text="Submit")
        submit_button.bind(on_release=self.submit_info)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def submit_info(self, instance):
        print(self.username.text)
        
        # Switch to Homepage screen after submission
        self.manager.current = "leaderboard"  # Switch to homepage screen

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