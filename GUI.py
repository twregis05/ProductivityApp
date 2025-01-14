import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        user_label = Label(text="Username")
        layout.add_widget(user_label)
        self.username = TextInput(multiline=False)
        layout.add_widget(self.username)

        pass_label = Label(text="Password")
        layout.add_widget(pass_label)
        self.password = TextInput(multiline=False)
        layout.add_widget(self.password)

        submit_button = Button(text="Submit")
        submit_button.bind(on_release=self.submit_info)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def submit_info(self, instance):
        print(self.username.text)

class MainAppScreen(Screen):
    pass

class AppScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)




class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(LoginScreen(name="login"))
        manager.add_widget(MainAppScreen(name="main"))
        return manager

if __name__ == "__main__":
    MyApp().run()


