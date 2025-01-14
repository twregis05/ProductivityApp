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
        # calling grid layout constructor
        super(LoginScreen, self).__init__(**kwargs)
        
         # Outer GridLayout with 2 rows
        outer_layout = GridLayout(cols=1, rows=2)

        # Inner GridLayout in the first row (3 rows and 2 columns)
        inner_layout = GridLayout(cols=2, rows=3)

        # First name field (Row 1, Column 1)
        inner_layout.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        inner_layout.add_widget(self.first_name)

        # Last name field (Row 2, Column 1)
        inner_layout.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        inner_layout.add_widget(self.last_name)

        # Email field (Row 3, Column 1)
        inner_layout.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        inner_layout.add_widget(self.email)

        # Add the inner layout (3 rows, 2 columns) to the first row of the outer layout
        outer_layout.add_widget(inner_layout)

        # Submit button (Second row of the outer layout)
        self.submit = Button(text="Submit", font_size=32, size=(100, 50))
        self.submit.bind(on_press=self.submit_data)

        # Add the submit button to the second row of the outer layout
        outer_layout.add_widget(self.submit)

        # Add the outer layout (with inner layout and submit button) to the screen
        self.add_widget(outer_layout)

    def submit_data(self, instance):
        # Get data from input fields
        first_name = self.first_name.text
        last_name = self.last_name.text
        print(f"Hello {first_name} {last_name}!")
        
        # Switch to Homepage screen after submission
        self.manager.current = "homepage"  # Switch to homepage screen

class MyApp(App):
    def build(self):
        # Create ScreenManager to manage different screens
        sm = ScreenManager()

        # Add window screens
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(Homepage(name="homepage"))
        sm.add_widget(Leaderboard(name="leaderboard"))
        sm.add_widget(Calendar(name="calendar"))
        sm.add_widget(Suggestion(name="suggestion"))
        sm.add_widget(Account(name="account"))

        
        return sm

if __name__ == "__main__":
    MyApp().run()