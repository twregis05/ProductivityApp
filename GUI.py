import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # calling grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # setting columns
        self.cols = 2

        # adding widgets
        self.add_widget(Label(text="First Name: "))
        
        # adding input box
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)

        self.add_widget(Label(text="Last Name: "))
        
        # adding input box
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

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


