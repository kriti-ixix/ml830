shoes = {36:5, 37:3, 38:0, 39:10, 40:1}
print("Enter quit to leave")

while True:
    userInput = input("What size shoe do you want? ")

    if userInput == "quit":
        break
    else:
        userInput = int(userInput)

    if shoes[userInput] == 0:
        print("Sorry, we are out of stock")
    else:
        print("Giving you a shoe of size", userInput)
        shoes[userInput] -= 1