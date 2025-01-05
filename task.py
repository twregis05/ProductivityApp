from datetime import datetime
class Task:

    def __init__(self, title: str, due_date: str, notes: str):
        self.title = "Untitled" if title is None else title
        if not self.set_due(due_date): self.due_date = None
        self.completed = False
        self.notes = notes

    def rename_task(self, title: str):
        if self.title == title:
            return False
        self.title = title
        return True
        

    def set_complete(self, completed: bool):
        self.completed = completed

    def set_due(self, due: str):
        try:
            if due == None: 
                self.due_date = due
                return True
            datetime.strptime(due, "%m/%d/%Y")
            self.due_date = due
            return True
        except ValueError:
            return False
            
    def edit_notes(self, notes: str):
        self.notes = notes

    def print_task(self):
        print("Task name: " + self.title)
        print("Due date: " + ("None" if self.due_date is None else self.due_date))
        print("Notes: " + ("None" if self.notes is None else self.notes))
        print("Completed? " + ("Yes" if self.completed else "No"))

        
