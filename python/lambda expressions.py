def times2(num):
    return num ** 2

myList = [1, 2, 3, 4]

outList = list(map(times2, myList))
#print(outList)

finalList = list(map(lambda num : num ** 2, outList))
print(finalList)
