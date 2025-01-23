from datetime import datetime
class Task:

    # Constructor for Task object
    def __init__(self, title: str, due_date: str, description: str):
        self.title = "Untitled" if title is None else title
        if not self.set_due(due_date): self.due_date = None
        self.completed = False
        self.description = description
        self.created_on = datetime.now().strftime("%m/%d/%Y")

    # Renames the task. Returns true if param is different to current
    # title, otherwise returns false
    def rename_task(self, title: str) -> bool:
        if self.title == title:
            return False
        self.title = title
        return True
        
    # Sets completed status (T/F) to parameter
    def set_complete(self, completed: bool):
        self.completed = completed

    # Sets task due date to parameter. 
    # If parameter is invalid (not in format MM/DD/YYYY) return false,
    # returns true if valid (MM/DD/YYYY or None)
    def set_due(self, due: str) -> bool:
        try:
            if due == None: 
                self.due_date = due
                return True
            datetime.strptime(due, "%m/%d/%Y")
            self.due_date = due
            return True
        except ValueError:
            return False

    # Sets task description to parameter     
    def edit_description(self, description: str):
        self.description = description

    # Prints data from task
    def print_task(self):
        print("Task name: " + self.title)
        print("Due date: " + ("None" if self.due_date is None else self.due_date))
        print("Description: " + ("None" if self.description is None else self.description))
        print("Completed? " + ("Yes" if self.completed else "No"))
        print(f"Date created: {self.created_on}")

        
