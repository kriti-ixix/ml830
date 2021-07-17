students = []
keys = ['Name', 'Roll No', 'Marks', 'Percentage']

for i in range(3):
    studentDict = {}

    for key in keys:
        if key == 'Name':
            studentDict[key] = input("Enter your " + key + ": ")
        elif key == 'Percentage':
            studentDict[key] = (studentDict['Marks'] * 100) / 50
        else:
            studentDict[key] = int(input("Enter your " + key + ": "))

    students.append(studentDict)

print(students)
