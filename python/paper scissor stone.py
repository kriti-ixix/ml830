import random 

player1 = input("Enter first player's name: ")
#player2 = input("Enter second player's name: ")
player2 = "Computer"

choices = ['paper', 'scissor', 'stone']
win1 = 0
win2 = 0

while True:

    try:
        if win1==2 or win2==2:
            break

        turn1 = input("First player's turn: ").lower()
        #turn2 = input("Second player's turn: ").lower()

        #if turn1 != 'paper' or turn1 != 'scissor' or turn1 != 'stone':

        if turn1 not in choices:
            raise ValueError

        turn2 = random.choice(choices)
        print("Computer's choice: " + turn2)

        winner = "Winner is "

        #First player's win
        if (turn1=="paper" and turn2=="stone") or (turn1=="scissor" and turn2=="paper") or (turn1=="stone" and turn2=="scissor"):
            winner += player1
            win1 += 1

        #Second player's win
        elif (turn2=="paper" and turn1=="stone") or (turn2=="scissor" and turn1=="paper") or (turn2=="stone" and turn1=="scissor"):
            winner += player2
            win2 += 1

        #Draw
        else:
            winner = "Draw"

        print(winner)

    except ValueError:
        print("The input was invalid")

    except:
        print("Error")


if win1==2:
    print("Our final winner is " + player1)
else:
    print("Our final winner is " + player2)