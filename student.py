"""
Student Class
"""


class Student:
    """
    Default Student Constructor
    """

    def __init__(self):
        self.gpa = 0.0
        self.stress = 50
        self.knowledge = 50
        self.dexterity = 50
        self.strength = 50
        self.speed = 50
        self.courses = []
        self.name = "Bob"

    def liftWeights(self, weightOfWeights):
        self.strength += weightOfWeights/20


    def runOnTreadmill(self, speedOfRun):
        if speedOfRun >= 3.5:
            self.speed += speedOfRun


    def addToStress(self, amt):
        self.setStress(amt + self.getStress())


    def getStress(self):
        return self.stress


    def setStress(self, stress):
        if 0 <= stress <= 100:
            self.stress = stress
        elif stress < 0:
            self.stress = 0
        elif stress > 100:
            self.stress = 100


    def getGPA(self):
        sum = 0
        for course in self.courses:
            sum += course.grade
        return sum / len(self.courses)


    def registerForCource(self, course):
        self.courses += course


    def dropCourse(self, course):
        self.courses.remove(course)


    def getGrades(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades

    def getName(self):
        return self.name


    def setName(self, name):
        self.name = name


    def getKnowledge(self):
        return self.knowledge


    def setKnowledge(self, know):
        if 0 <= know <= 100:
            self.knowledge = know
        elif know < 0:
            self.knowledge = 0
        elif know > 100:
            self.knowledge = 100


    def addKnowledge(self, know):
        self.setKnowledge(know + self.getKnowledge())



