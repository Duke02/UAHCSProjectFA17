import datetime

class Course:

    def __init__(self):
        self.startTime = datetime.timedelta(hours=8, minutes=00) # 0 minutes after 8am bc I have no idea how to do time
                            # and it's getting kinda late for me and my 8am class
                            # in the morning.
        self.length = datetime.timedelta(minutes=55)
        self.endTime = self.startTime + self.length # ie 8:55
        self.days = "MTWF" # days of the week the class meets
        self.testDates = []
        self.grade = 90 # Hopefully
