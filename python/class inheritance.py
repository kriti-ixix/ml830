class Student: #Base/Parent class
    def __init__(self, n, r):
        self.name = n
        self.rollno = r


class Exams(Student): #Derived/Child class
    def __init__(self, n, r, s, m):
        Student.__init__(self, n, r)
        self.subject = s
        self.marks = m
        self.percentage = 0

    def calPercentage(self):
        self.percentage = (self.marks * 100) / 50

    def __str__(self):
        return self.name + " got " + str(self.percentage) + " in " + self.subject


english = Exams("ABC", 10, "English", 45)
english.calPercentage()

print(english)