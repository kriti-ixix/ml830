myDict = {'a':10, 'b':20, 5:'xyz', 10:False, 'z':[1, 2, 3, 4]}

#print(myDict['z'])
#print(myDict[10])

myDict['k'] = 20
#print(myDict)

myDict[10] = "Hello"
#print(myDict)

newDict = {}

for x in range(5):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    newDict[key] = value

#print(newDict)

for x in myDict: #Returns only the keys
    print(x)

for x in myDict.values(): #Returns only the values
    print(x)

for x in myDict.items(): #Returns both the keys and the values in a tuple
    print(x)

for (x, y) in myDict.items(): #Dictionary unpacking
    print("Key:", x, "Value:", y)