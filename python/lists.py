myList = ["ABC", "XYZ", 1, 5, 10.293, True, "HELLO"]

print(myList)

print(myList[0])

myList[1] = "PQR"
print(myList)
print(myList[:4]) #List Slicing

myList.append(10)
print(myList)

myList.insert(0, 100)
print(myList)

myList.pop()
print(myList)

myList.pop(2)
print(myList)

print(len(myList))

print(myList.index(5))

newList = []

for i in range(5):
    x = input("Enter a value: ")
    newList.append(x)

print(newList)

for x in myList:
    print(x)

#Nested Lists
nestedList = [1 , 2, [3, 4, 5], 6, 7]
print(nestedList[0])
print(nestedList[2])
print(nestedList[2][1][0])

numList = [1, 45, 239, 400, 100, 56, 20]

for num in numList:
    if num%2 != 0:
        print(num)