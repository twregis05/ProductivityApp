from task import Task

def test1():
    task1 = Task("Mow lawn", "02/05/2025", "Must get done tonight")
    task1.print_task()

    print("\nCompleting task 1:")
    task1.set_complete(True)
    task1.print_task()

    print("\nChanging title")
    task1.rename_task("")

    task2 = Task("Fake task", "This is not a due date", None)
    task2.print_task()

def main():
    test1()


main()