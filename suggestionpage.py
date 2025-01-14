import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class Suggestion(Screen):
    def __init__(self, **kwargs):
        super(Suggestion, self).__init__(**kwargs)
        
        # Simple label to show on the Suggestion screen
        label = Label(text="Welcome to Suggestion!", font_size=40)
        self.add_widget(label)
