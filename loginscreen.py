import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        user_label = Label(text="Username", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "y": 0.7})
        layout.add_widget(user_label)
        self.username = TextInput(multiline=False, size_hint=(0.6, 0.1), pos_hint={"x": 0.3, "y": 0.7})
        layout.add_widget(self.username)

        pass_label = Label(text="Password", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "y": 0.5})
        layout.add_widget(pass_label)
        self.password = TextInput(multiline=False, password=True, size_hint=(0.6, 0.1), pos_hint={"x": 0.3, "y": 0.5})
        layout.add_widget(self.password)

        submit_button = Button(text="Submit", size_hint=(0.4, 0.1), pos_hint={"x": 0.3, "y": 0.3})
        submit_button.bind(on_release=self.submit_info)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def submit_info(self, instance):
        print(self.username.text)
        
        # Switch to Homepage screen after submission
        self.manager.current = "main"  # Switch to homepage screen