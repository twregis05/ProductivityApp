import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Leaderboard(Screen):
    def __init__(self, **kwargs):
        super(Leaderboard, self).__init__(**kwargs)
        grid = GridLayout(cols=1, rows=1)
        grid.add_widget(Label(text="Leaderboard"))
        self.add_widget(grid)