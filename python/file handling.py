'''
Three modes to open a file:
- r -> Read a file
- w -> Write to a new file or overwrite an existing file
- a -> Append to a file
'''

vacationPlaces = ['New York', 'Paris', 'Mumbai', 'Rome', 'London']

'''
myFile = open('file.txt', 'w')
myFile.write("How are you")
myFile.close()

myFile = open('file.txt', 'r')
contentsOfFile = myFile.read()
print(contentsOfFile)
myFile.close()
'''

# vacationFile = open('vacation.txt', 'w')

# for city in vacationPlaces:
#     vacationFile.write(city + "\n")

# vacationFile.close()

# vacationFile = open('vacation.txt', 'a')
# vacationFile.write("Tokyo")
# vacationFile.close()

# vacationFile = open('vacation.txt', 'r')
# vacationContent = vacationFile.read() #Reads the entire file in one go 
# print(vacationContent)

# for line in vacationFile:
#     print(line, end="")

# print(vacationFile.readline())
# print(vacationFile.readline())

with open('vacation.txt', 'r') as vacationFile:
    for line in vacationFile:
        print(line, end="")
    print()