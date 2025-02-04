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
from functools import partial  #partial for passing arguments




class Calendar(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        self.pageGrid = GridLayout(cols=1, rows=3)

        self.switchLayout = FloatLayout()
        self.calendarLayout = FloatLayout()
        self.tasksLayout = FloatLayout()
       
        #Switch Buttons
        self.calendarButton = Button(text="Calendar", size_hint=(0.15,0.15), pos_hint={"x": 0.68, "y": 0.8})
        self.listButton = Button(text="List", size_hint=(0.15,0.15), pos_hint={"x": 0.83, "y": 0.8})

        # Bind button actions to screen transitions
        self.calendarButton.bind(on_press=self.switch_to_calendar)
        self.listButton.bind(on_press=self.switch_to_list)

        self.switchLayout.add_widget(self.calendarButton)
        self.switchLayout.add_widget(self.listButton)
        self.pageGrid.add_widget(self.switchLayout)
       
        self.switch_to_calendar(None)

        self.add_widget(self.pageGrid)

    def updateCalendar(self, chosenMonth, chosenYear):
        self.calendarGrid = GridLayout(cols=1, rows=3, pos_hint={"x": 0.1, "y": 0.8}, size_hint=(0.8,1))
        self.calendarGrid.add_widget(Label(text="Calendar", pos_hint={"x":0.5, "y":0.5}))

        self.monthBox = BoxLayout(size_hint=(0.5, 1))
        self.monthLabel = Button(text=f"{calendar.month_name[chosenMonth]} {chosenYear}")
        
        self.leftMonth = Button(text="Left")
        self.rightMonth = Button(text="Right")
        
        # Bind the buttons to update the month
        self.leftMonth.bind(on_press=lambda instance: self.prev_month(chosenMonth, chosenYear, instance))
        self.rightMonth.bind(on_press=lambda instance: self.next_month(chosenMonth, chosenYear, instance))
        
        self.monthBox.add_widget(self.leftMonth)
        self.monthBox.add_widget(self.monthLabel)
        self.monthBox.add_widget(self.rightMonth)
        self.calendarGrid.add_widget(self.monthBox)

        self.dayGrid = GridLayout(rows=7, cols=7, spacing=60)
        self.dayGrid.add_widget(Label(text="SUN", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="MON", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="TUE", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="WED", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="TH", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="FRI", pos_hint={"x": 0.5, "y": 0.5}))
        self.dayGrid.add_widget(Label(text="SAT", pos_hint={"x": 0.5, "y": 0.5}))

        # Gets days of the month
        month_days = calendar.monthcalendar(chosenYear, chosenMonth)

        # Add the days of the month to the grid
        daysList = []
        for week in month_days:
            for day in week:
                daysList.append(day)

       

        for day in range(len(daysList)):
            if daysList[day] != 0:
                daysList[day] -= 1
        
        
        for day in range(len(daysList)):

            self.dateLayout = FloatLayout()
            self.taskDateLayout = GridLayout(rows=3, cols=1)
            if daysList[day] != 0:
                self.dateLayout.add_widget(Label(text=str(daysList[day]), pos_hint={"x": 0.4, "y": 1}))
            else:
                self.dateLayout.add_widget(Label(text="", pos_hint={"x": 0.1, "y": 0.1}))
               
            self.dayGrid.add_widget(self.dateLayout)
             

      
        self.calendarGrid.add_widget(self.dayGrid)
        self.calendarLayout.add_widget(self.calendarGrid)


    def switch_to_list(self, instance):
         # Change the content to List view
        self.calendarLayout.clear_widgets()  # Clear the current calendar view

        # Update the page grid with the new content
        self.pageGrid.clear_widgets()
        self.pageGrid.add_widget(self.switchLayout)
        list_label = Label(text="This is the List Page", size_hint=(1, 1), pos_hint={"x": 0, "y": 0.5})
        self.pageGrid.add_widget(list_label)
        self.addTasks()


    def switch_to_calendar(self, instance):
        self.pageGrid.clear_widgets()
        self.pageGrid.add_widget(self.switchLayout)
        self.calendarLayout.clear_widgets()

        # Initialize the current month and year
        defaultMonth = datetime.datetime.now().month
        defaultYear = datetime.datetime.now().year

        self.updateCalendar(defaultMonth, defaultYear)

        self.pageGrid.add_widget(self.calendarLayout)
        self.addTasks()
    
    def addTasks(self):
        # Update the task layout (for adding tasks and goals)
        self.tasksLayout.clear_widgets()
         # Task Layout for adding tasks
        self.addTaskLayout = BoxLayout(orientation="horizontal", size_hint=(0.3, 0.25), pos_hint={"x": 0, "y": 0.2})
        self.addTaskLayout.add_widget(Label(text="Add Task"))
        self.addTaskLayout.add_widget(Button(text="+", size_hint=(0.2, 0.5), pos_hint={"y": 0.3}))

        # Goal Layout for adding goals
        self.addGoalLayout = BoxLayout(orientation="horizontal", size_hint=(0.3, 0.25), pos_hint={"x": 0, "y": 0.05})
        self.addGoalLayout.add_widget(Label(text="Add Goal"))
        self.addGoalLayout.add_widget(Button(text="+", size_hint=(0.2, 0.5), pos_hint={"y": 0.3}))

        # Add the task and goal layouts
        self.tasksLayout.add_widget(self.addTaskLayout)
        self.tasksLayout.add_widget(self.addGoalLayout)

        self.pageGrid.add_widget(self.tasksLayout)

    def prev_month(self, chosenMonth, chosenYear, instance):
        print("Previous Month")
         # Update the current month
        if chosenMonth == 1:
            chosenMonth = 12
            chosenYear -= 1
        else:
            chosenMonth -= 1
        
        self.dayGrid.clear_widgets()
        # Update the calendar view
        self.updateCalendar(chosenMonth, chosenYear)
        
    def next_month(self, chosenMonth, chosenYear, instance):
        print("Next Month")
        """Switches to the next month."""
        # Update the current month
        if chosenMonth == 12:
            chosenMonth = 1
            chosenYear += 1
        else:
            chosenMonth += 1
        
        self.dayGrid.clear_widgets()
        # Update the calendar view
        self.updateCalendar(chosenMonth, chosenYear)