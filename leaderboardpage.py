import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Leaderboard(Screen):
    def __init__(self, **kwargs):
        super(Leaderboard, self).__init__(**kwargs)

        outer_layout = GridLayout(cols=1, rows=2)

        row1 = FloatLayout()
        row2 = GridLayout(cols=5, rows=1) 

        
        # Simple label to show on the leaderboard screen
        label = Label(text="Welcome to Leaderboard!", font_size=40, size_hint=(None, None), size=(400, 100), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        row1.add_widget(label)
        calendarBut = Button(text="Calendar", font_size=16, size=(50, 50))
        leaderBut = Button(text="LeaderBoard", font_size=16, size=(50, 50))
        homepageBut = Button(text="HomePage", font_size=16, size=(50, 50))
        suggestionBut = Button(text="Suggestion", font_size=16, size=(50, 50))
        profileBut = Button(text="Account", font_size=16, size=(50, 50))
        row2.add_widget(calendarBut)
        row2.add_widget(leaderBut)
        row2.add_widget(homepageBut)
        row2.add_widget(suggestionBut)
        row2.add_widget(profileBut)

        # Bind the buttons to their corresponding functions
        calendarBut.bind(on_press=self.on_calendar_click)
        leaderBut.bind(on_press=self.on_leaderboard_click)
        homepageBut.bind(on_press=self.on_homepage_click)
        suggestionBut.bind(on_press=self.on_suggestion_click)
        profileBut.bind(on_press=self.on_profile_click)

        outer_layout.add_widget(row1)
        outer_layout.add_widget(row2)


        self.add_widget(outer_layout)
    
    def on_calendar_click(self, instance):
        self.manager.current = "calendar"

    def on_leaderboard_click(self, instance):
        self.manager.current = "leaderboard"

    def on_homepage_click(self, instance):
        self.manager.current = "homepage"

    def on_suggestion_click(self, instance):\
        self.manager.current = "suggestion"

    def on_profile_click(self, instance):
        self.manager.current = "profile"
