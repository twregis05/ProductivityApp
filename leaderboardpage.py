import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class Leaderboard(Screen):
    def __init__(self, **kwargs):
        super(Leaderboard, self).__init__(**kwargs)
        
        # Simple label to show on the leaderboard screen
        label = Label(text="Welcome to Leaderboard!", font_size=40)
        self.add_widget(label)
