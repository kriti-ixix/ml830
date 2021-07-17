import random

class ValueTooLargeError(Exception):
    pass

class ValueTooSmallError(Exception):
    pass


guess = random.randint(1, 10)

while True:

    try:
        userInput = int(input("Enter a guess: "))

        if userInput < guess:
            raise ValueTooSmallError
        elif userInput > guess:
            raise ValueTooLargeError
        else:
            print("Your guess was correct")
            break

    except ValueTooLargeError:
        print("Your guess was too large")

    except ValueTooSmallError:
        print("Your guess was too small")

    except:
        print("Error occurred")
