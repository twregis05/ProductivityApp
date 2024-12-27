class Task:
    def __init__(self, title, due_date, notes):
        self.title = "Untitled" if title is None else title
        self.due_date = due_date
        self.completed = False
        self.notes = notes

    def complete(self):
        self.completed = True

    