import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class Account(Screen):
    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)
        
        # Simple label to show on the Account screen
        label = Label(text="Welcome to Account!", font_size=40)
        self.add_widget(label)
