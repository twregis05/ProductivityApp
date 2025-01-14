import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class Calendar(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        
        # Simple label to show on the Calendar screen
        label = Label(text="Welcome to Calendar!", font_size=40)
        self.add_widget(label)

