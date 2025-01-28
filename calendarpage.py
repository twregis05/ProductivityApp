import kivy
import calendar
import datetime
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock



class Calendar(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        self.pageGrid = GridLayout(cols=1, rows=3)

        self.switchLayout = FloatLayout()
        self.calendarLayout = FloatLayout()
        self.tasksLayout = FloatLayout()
       
        #Switch Buttons
        self.calendarButton = Button(text="Calendar", size_hint=(0.15,0.15), pos_hint={"x": 0.68, "y": 0.75})
        self.listButton = Button(text="List", size_hint=(0.15,0.15), pos_hint={"x": 0.83, "y": 0.75})

        # Bind button actions to screen transitions
        self.calendarButton.bind(on_press=self.switch_to_calendar)
        self.listButton.bind(on_press=self.switch_to_list)

        self.switchLayout.add_widget(self.calendarButton)
        self.switchLayout.add_widget(self.listButton)
        self.pageGrid.add_widget(self.switchLayout)
       
        self.switch_to_calendar(None)

        self.add_widget(self.pageGrid)

    def updateCalendar(self):
        self.calendarGrid = GridLayout(cols=1, rows=3, pos_hint={"x": 0, "y": 0.65})
        self.calendarGrid.add_widget(Label(text="Calendar", pos_hint={"x":0.5, "y":0.5}))
        
        now = datetime.datetime.now()
        self.currMonth = now.month
        self.currYear = now.year

        self.monthLayout = FloatLayout()
        self.monthBox = BoxLayout(size_hint=(0.5, 1))
        self.monthLabel = Button(text=f"{calendar.month_name[self.currMonth]} {self.currYear}", size_hint=(0.12, 0.01), pos_hint={"x": 0.4, "y": 0.5})
        self.leftMonth = Button(text="<-", size_hint=(0.01, 0.01), pos_hint={"x": 0.3, "y": 0.5})
        self.rightMonth = Button(text="->", size_hint=(0.01, 0.01), pos_hint={"x": 0.6, "y": 0.5})
        
        
        self.monthBox.add_widget(self.leftMonth)
        self.monthBox.add_widget(self.monthLabel)
        self.monthBox.add_widget(self.rightMonth)
        self.calendarGrid.add_widget(self.monthBox)

        self.dayGrid = GridLayout(rows=6, cols=7, spacing=50)
        self.dayGrid.add_widget(Label(text="SUN", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="MON", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="TUE", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="WED", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="TH", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="FRI", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="SAT", pos_hint={"x": 0.5, "y": 0.5}))

        # Gets days of the month
        month_days = calendar.monthcalendar(self.currYear, self.currMonth)

        # Add the days of the month to the grid
        for week in month_days:
            for day in week:
                self.dayLayout = GridLayout(rows=2, cols=1)
                self.dayFloat = FloatLayout()
                self.dayLayout.add_widget(self.dayFloat)
                self.taskFloat = FloatLayout()
                self.dayLayout.add_widget(self.taskFloat)

                if day == 0:
                    # Add empty labels for the days outside of the current month
                    self.dayFloat.add_widget(Label(text=""))
                else:
                    self.dayFloat.add_widget(Label(text=str(day), pos_hint={"x": 1, "y": 0.5}))
                self.dayGrid.add_widget(self.dayLayout)
        
        self.calendarGrid.add_widget(self.dayGrid)
        self.calendarLayout.add_widget(self.calendarGrid)


    def switch_to_list(self, instance):
         # Change the content to List view
        self.calendarLayout.clear_widgets()  # Clear the current calendar view

        # Update the task layout (for adding tasks and goals)
        self.tasksLayout.clear_widgets()
         # Task Layout for adding tasks
        self.addTaskLayout = BoxLayout(orientation="horizontal", size_hint=(0.3, 0.25), pos_hint={"x": 0, "y": 0.4})
        self.addTaskLayout.add_widget(Label(text="Add Task"))
        self.addTaskLayout.add_widget(Button(text="+", size_hint=(0.2, 0.5), pos_hint={"y": 0.3}))

        # Goal Layout for adding goals
        self.addGoalLayout = BoxLayout(orientation="horizontal", size_hint=(0.3, 0.25), pos_hint={"x": 0, "y": 0.1})
        self.addGoalLayout.add_widget(Label(text="Add Goal"))
        self.addGoalLayout.add_widget(Button(text="+", size_hint=(0.2, 0.5), pos_hint={"y": 0.3}))

        # Add the task and goal layouts
        self.tasksLayout.add_widget(self.addTaskLayout)
        self.tasksLayout.add_widget(self.addGoalLayout)

        # Update the page grid with the new content
        self.pageGrid.clear_widgets()
        self.pageGrid.add_widget(self.switchLayout)
        list_label = Label(text="This is the List Page", size_hint=(1, 1), pos_hint={"x": 0, "y": 0.5})
        self.pageGrid.add_widget(list_label)
        self.pageGrid.add_widget(self.tasksLayout)


    def switch_to_calendar(self, instance):
        self.pageGrid.clear_widgets()
        self.pageGrid.add_widget(self.switchLayout)
        self.calendarLayout.clear_widgets()
        self.updateCalendar()

        self.pageGrid.add_widget(self.calendarLayout)
        self.pageGrid.add_widget(self.tasksLayout)