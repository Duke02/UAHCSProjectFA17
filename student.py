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
        self.stress = 50
        self.knowledge = 50
        self.dexterity = 50
        self.strength = 50
        self.speed = 50
        self.courses = []

    def liftWeights(self, weightOfWeights):
        self.strength += weightOfWeights/20

    def runOnTreadmill(self, speedOfRun):
        if speedOfRun >= 3.5:
            self.speed += speedOfRun

    def addToStress(self, amt):
        if self.stress + amt >= 100:
            self.stress = 100
        elif self.stress + amt <= 0:
            # ie amt is negative
            self.stress = 0
        else:
            self.stress += amt

    def setStress(self, stress):
        if 0 <= stress <= 100:
            self.stress = stress

    def getGPA(self):
        sum = 0
        for clazz in self.classes:
            sum += clazz.grade
        return sum / len(self.classes)

    def registerForClass(self, clazz):
        self.classes += clazz

