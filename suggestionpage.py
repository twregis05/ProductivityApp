import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Suggestion(Screen):
    def __init__(self, **kwargs):
        super(Suggestion, self).__init__(**kwargs)
        grid = GridLayout(cols=1, rows=1)
        grid.add_widget(Label(text="Suggestions Page"))
        self.add_widget(grid)