testList = [1, 2, 3, 4, 4, 1, 5]
#print(testList)
mySet = {"ABC", 5, 6, 7, 7, 10, True}
mySet.add("PQR")
print(mySet)

outputList = list(set(testList))
#print(outputList)

if "ABC" in mySet:
    print("Found it")