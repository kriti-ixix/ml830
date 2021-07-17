import traceback

try: #Normal execution of the program
    myList = [1, 2, 3, 4]
    print(myList[2])
    #print(myList[10])

    myDict = {1:'a', 2:'b', 3:'c', 4:'d'}
    print(myDict[2])
    print(myDict[10])

except ValueError:
    print("ValueError occurred")

except IndexError:
    print("IndexError occurred")

except KeyError:
    print("KeyError occurred")

except Exception as e: #In case of any error
    #print(e)
    traceback.print_exc()
