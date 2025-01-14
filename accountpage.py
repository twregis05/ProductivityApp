import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Account(Screen):
    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)
        grid = GridLayout(cols=1, rows=1)
        grid.add_widget(Label(text="Account Page"))
        self.add_widget(grid)