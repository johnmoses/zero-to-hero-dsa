""" 
Design a task manager
Implement a basic task manager with the following operations:
    
    Add a task with a name, priority, and deadline
    Get the next task with the highest priority and earliest deadline
    Remove a task with a given name
    Get all tasks
"""
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority, deadline):
        self.tasks.append((name, priority, deadline))

    def get_next_task(self):
        if not self.tasks:
            return None
        self.tasks.sort(key=lambda x: (x[1], x[2]))
        return self.tasks.pop(0)

    def remove_task(self, name):
        for i, task in enumerate(self.tasks):
            if task[0] == name:
                self.tasks.pop(i)
                break

    def get_tasks(self):
        return self.tasks

task_manager = TaskManager()
task_manager.add_task("Task 1", 1, "2022-01-01")
task_manager.add_task("Task 2", 2, "2022-02-01")
task_manager.add_task("Task 3", 1, "2022-03-01")
print(task_manager.get_next_task())
print(task_manager.get_next_task())  # ("Task 3", 1, "2022-03-01")
task_manager.remove_task("Task 1")
print(task_manager.get_tasks())