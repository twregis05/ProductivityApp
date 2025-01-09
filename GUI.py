import kivy
import sqlite3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # calling grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()

        # setting columns for text fields and labels
        self.inside.cols = 2

        # adding first name label
        self.inside.add_widget(Label(text="First Name: "))
        
        # adding input box
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name: "))
        
        # adding input box
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        # Adding whole field to top row of GUI
        self.add_widget(self.inside)

        
        
        # Adding a submit button
        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.submit_data)
        self.add_widget(self.submit)

    def submit_data(self, instance):
        first_name = self.first_name.text
        last_name = self.last_name.text
        print(f"Hello {first_name} {last_name}!")



class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()


