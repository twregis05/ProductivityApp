import kivy
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar  # Import ProgressBar




class Homepage(Screen):
    def __init__(self, **kwargs):
        super(Homepage, self).__init__(**kwargs)
        floatLayout = FloatLayout()

        #To-Do-List Section
        listTitle= Label(text="To-Do-List", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "y": 0.9})
        task1 = Label(text="Task #1: ", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "y": 0.8})
        task2 = Label(text="Task #2: ", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "y": 0.7})
        task3 = Label(text="Task #3: ", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "y": 0.6})
        moreButton = Button(text="More", size_hint=(0.4, 0.1), pos_hint={"x": 0.3, "y": 0.5})

        doListGrid = GridLayout(cols=1, rows=5, size_hint=(0.35, 0.45), pos_hint={"x": 0.01, "y": 0.54})
        doListGrid.add_widget(listTitle)
        doListGrid.add_widget(task1)
        doListGrid.add_widget(task2)
        doListGrid.add_widget(task3)
        doListGrid.add_widget(moreButton)

        #Summary Section:
        summaryTable = GridLayout(cols=1, rows=3, size_hint=(0.6, 0.75), pos_hint={"x": 0.39, "y": 0.23})
        summaryTitle = Label(text="Summary", size_hint=(0.2, 0.1))
        tasksGrid = GridLayout(cols=3,rows=11)
        tasksGrid.add_widget(Label(text="Tasks"))
        tasksGrid.add_widget(Label(text="Status"))
        tasksGrid.add_widget(Label(text="Date Completed"))

        for i in range(1, 11):
            task = "Task #" + str(i) + ":"
            tasksGrid.add_widget(Label(text=task))
            tasksGrid.add_widget(Label(text="none"))
            tasksGrid.add_widget(Label(text="UNCOMPLETED"))

        moreTasks = Button(text="...", size_hint=(0.2, 0.05))

        summaryTable.add_widget(summaryTitle)
        summaryTable.add_widget(tasksGrid)
        summaryTable.add_widget(moreTasks)

        #Timer Section
        timerButton = Button(text="TIMER", size_hint=(0.3,0.1), pos_hint={"x": 0.01, "y": 0.38})
        timerButton.pos = (20, 240)
        #Add pop-up code below:

        #Streak Section
        streakLayout = BoxLayout(orientation="horizontal", size_hint=(0.4,0.1), pos_hint={"x": 0.01, "y": 0.25})
        streakLayout.add_widget(Label(text="Streak: ", size_hint=(None, 1), width=100))

        #Progress Bar Sectiom
       #progressLayout = BoxLayout(orientation="horizontal", pos_hint={"x": 0.2,"y": 0})
        progress = ProgressBar(size_hint=(0.9, 0.1), size=(600, 20), pos_hint={"x": 0.06, "y": 0.1})
        progress.value = 50  
      # progressLayout.add_widget(progress)

        floatLayout.add_widget(doListGrid)
        floatLayout.add_widget(timerButton)
        floatLayout.add_widget(summaryTable)
        floatLayout.add_widget(streakLayout)
        floatLayout.add_widget(progress)  



        self.add_widget(floatLayout)


