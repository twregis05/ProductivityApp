import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout


class Homepage(Screen):
    def __init__(self, **kwargs):
        super(Homepage, self).__init__(**kwargs)
        
        outer_layout = GridLayout(cols=1, rows=2)

        row1 = FloatLayout()
        row2 = GridLayout(cols=5, rows=1) 

        # Simple label to show on the homepage screen
        label = Label(text="Welcome to the Homepage!", font_size=40)
        row1.add_widget(label)

        outer_layout.add_widget(row1)
        outer_layout.add_widget(row2)

        self.add_widget(outer_layout)


