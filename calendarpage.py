import kivy
import calendar
import datetime
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class Calendar(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        pageGrid = GridLayout(cols=1, rows=3)

        switchLayout = FloatLayout()
        calendarLayout = FloatLayout()
        tasksLayout = FloatLayout()
       
        #Switch Buttons
        calendarButton = Button(text="Calendar", size_hint=(0.15,0.15), pos_hint={"x": 0.68, "y": 0.75})
        listButton = Button(text="List", size_hint=(0.15,0.15), pos_hint={"x": 0.83, "y": 0.75})

        switchLayout.add_widget(calendarButton)
        switchLayout.add_widget(listButton)

        #Calendar
        self.calendarGrid = GridLayout(cols=1, rows=3, pos_hint={"x": 0, "y": 0.65})
        self.calendarGrid.add_widget(Label(text="Calendar"))
        self.updateCalendar()
        calendarLayout.add_widget(self.calendarGrid)

        pageGrid.add_widget(switchLayout)
        pageGrid.add_widget(calendarLayout)
        pageGrid.add_widget(tasksLayout)

        self.add_widget(pageGrid)

    def updateCalendar(self):
        now = datetime.datetime.now()
        self.currMonth = now.month
        self.currYear = now.year

        self.monthLayout = FloatLayout()
        self.leftMonth = Button(text="<-", size_hint=(0.1,0.1), pos_hint={"x": 0.2})
        self.rightMonth = Button(text="->", size_hint=(0.1,0.1), pos_hint={"x": 0.8})
        self.monthLabel = Label(text=f"{calendar.month_name[self.currMonth]} {self.currYear}", pos_hint={"x":0.5})
        self.monthLayout.add_widget(self.leftMonth)
        self.monthLayout.add_widget(self.monthLabel)
        self.monthLayout.add_widget(self.rightMonth)
        self.calendarGrid.add_widget(self.monthLayout)

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
