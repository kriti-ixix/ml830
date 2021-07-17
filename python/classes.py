class Student:
    def __init__(self, n, m, r="N/A"):
        self.name = n
        self.marks = m
        self.rollno = r
        self.percentage = 0

    def calPercentage(self):
        self.percentage = (self.marks * 100) / 50

    def __str__(self):
        #11. XYZ got 35 marks with 80%
        return str(self.rollno) + ". " + self.name + " got " + str(self.marks) + " with " + str(self.percentage) + "%"


student1 = Student("ABC", 40, 10)
student2 = Student("XYZ", 35, 11)
student3 = Student("JKL", 35)

student1.calPercentage()
#print(student1.percentage)

student2.calPercentage()
student3.calPercentage()

print(student1)
print(student2)
print(student3)