"""
Student Class
"""


class Student:
    """
    Default Student Constructor
    """

    def __init__(self):
        self.classes = []
        self.gpa = 0.0
        self.morale = 50

    """
    Class attendance increases upon going to class
    """

    def goToClass(self, whichClass):
        whichClass.attendance += 1

    """
    Or be responsible and finish a task and feel accomplished, boosting morale
    """

    def adult(self, task):
        task.completed = True
        self.morale += 10
