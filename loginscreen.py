import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Entire screen layout will be a FloatLayout
        layout = FloatLayout()

        # Label representing username
        user_label = Label(
            text="Email or Username", 
            size_hint=(0.1, 0.1), 
            pos_hint={"x": 0.23, "y": 0.8})
        layout.add_widget(user_label)
        # Textbox representing username
        self.username = TextInput(
            multiline=False, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.7})
        layout.add_widget(self.username)

        # Label representing password
        pass_label = Label(
            text="Password", 
            size_hint=(0.1, 0.1), 
            pos_hint={"x": 0.195, "y": 0.6})
        layout.add_widget(pass_label)
        # Textbox representing password
        self.password = TextInput(
            multiline=False, 
            password=True, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.5})
        layout.add_widget(self.password)

        # Button for login
        login_button = Button(
            text="Login", 
            size_hint=(0.4, 0.1), 
            pos_hint={"x": 0.3, "y": 0.3})
        # Button executes submit_info() function on release
        login_button.bind(on_release=self.submit_info)
        layout.add_widget(login_button)

        sign_up_label = Label(
            text="Don't have an account?",
            size_hint=(0.4, 0.1),
            pos_hint={"x":0.27, "y": 0.15}
        )

        layout.add_widget(sign_up_label)

        sign_up_link = ClickableText(
            text="[u][color=0000ff]Sign up![/color][/u]", 
            markup=True, 
            on_press=self.sign_up,
            size_hint=(0.4, 0.1),
            pos_hint={"x":0.405, "y": 0.15})
        layout.add_widget(sign_up_link)
        self.add_widget(layout)

    def submit_info(self, instance):
        # Switch to Homepage screen after submission
        self.manager.current = "main"  # Switch to homepage screen

    def sign_up(self, instance):
        self.manager.current = "signup" 



class ClickableText(ButtonBehavior, Label):
    pass
       

class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        sign_up_label = Label(
            text="Get Started with ProDucktive",
            font_name="Roboto", 
            size_hint=(0.3, 0.3), 
            pos_hint={"x": 0.35, "y": 0.8}, 
            font_size=60)
        layout.add_widget(sign_up_label)

        login_option = Label(
            text="Already have an account?",
            size_hint=(0.4, 0.1),
            pos_hint={"x":0.27, "y": 0.8}
        )

        layout.add_widget(login_option)

        login_link = ClickableText(
            text="[u][color=0000ff]Log in![/color][/u]", 
            markup=True, 
            on_press=self.login,
            size_hint=(0.4, 0.1),
            pos_hint={"x":0.408, "y": 0.8})
        layout.add_widget(login_link)
        self.add_widget(layout)

        first_name_label = Label(
            text="First name", 
            size_hint=(0.1, 0.1), 
            pos_hint={"x": 0.2, "y": 0.7})
        
        layout.add_widget(first_name_label)
        
        self.first_name = TextInput(
            multiline=False, 
            size_hint=(0.2, 0.05), 
            pos_hint={"x": 0.2, "y": 0.685})
        layout.add_widget(self.first_name)
        
        last_name_label = Label(
            text="Last name", 
            size_hint=(0.1, 0.1), 
            pos_hint={"x": 0.55, "y": 0.7})
        layout.add_widget(last_name_label)

        self.last_name = TextInput(
            multiline=False, 
            size_hint=(0.2, 0.05), 
            pos_hint={"x": 0.55, "y": 0.685})
        layout.add_widget(self.last_name)


        email_label = Label(
            text="Email", 
            size_hint=(0.05, 0.1), 
            pos_hint={"x": 0.2, "y": 0.6})
        layout.add_widget(email_label)

        self.email = TextInput(
            multiline=False, 
            size_hint=(0.6, 0.05), 
            pos_hint={"x": 0.2, "y": 0.585})
        layout.add_widget(self.email)

        user_label = Label(
            text="Username", 
            size_hint=(0.1, 0.1), 
            pos_hint={"x": 0.193, "y": 0.5})
        layout.add_widget(user_label)

        self.username = TextInput(
            multiline=False,  
            size_hint=(0.6, 0.05), 
            pos_hint={"x": 0.2, "y": 0.485})
        layout.add_widget(self.username)

        pass_label = Label(
            text="Password", 
            size_hint=(0.1, 0.1), 
            pos_hint={"x": 0.193, "y": 0.4})
        layout.add_widget(pass_label)
        
        self.password = TextInput(
            multiline=False, 
            password=True, 
            size_hint=(0.6, 0.05), 
            pos_hint={"x": 0.2, "y": 0.385})
        layout.add_widget(self.password)
        
        confirm_label = Label(
            text="Confirm Password", 
            size_hint=(0.15, 0.1), 
            pos_hint={"x": 0.2, "y": 0.3})
        layout.add_widget(confirm_label)
        
        self.confirm_password = TextInput(
            multiline=False, 
            password=True, 
            size_hint=(0.6, 0.05), 
            pos_hint={"x": 0.2, "y": 0.285})
        layout.add_widget(self.confirm_password)

        submit_button = Button(
            text="Sign Up", 
            size_hint=(0.4, 0.1), 
            pos_hint={"x": 0.3, "y": 0.15})
        
        submit_button.bind(on_release=self.login)
        layout.add_widget(submit_button)

    def login(self, instance):
        self.manager.current = "login"