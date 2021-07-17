#Importing the libraries
import os


#Global Variables
theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ','6': ' ', '7': ' ', '8': ' ', '9': ' '}


#User-Defined Functions
def clearScreen():
    if os.name == 'posix': #UNIX Operating System
        _ = os.system('clear')
    else: #Windows Operating System
        _ = os.system('cls')


def printBoard(board):
    print("")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("")


def playGame():
    turn = 'X'
    count = 0

    while True:
        printBoard(theBoard)

        if count == 9:
            print("No winner")
            break
        
        try:
            move = input(turn + "'s turn: ")

            if theBoard[move] == ' ':
                theBoard[move] = turn
                winner = checkWin(turn)
            
                if winner == turn:
                    printBoard(theBoard)
                    print("The winner is " + turn)
                    break

                else:
                    count += 1
                    if turn == 'X': 
                        turn = 'O'
                    else:
                        turn = 'X'


            else:
                print("That place is already filled") 

        except KeyError:
            print("The input is invalid")
        
        except:
            print("Error")


def checkWin(turn):
    winner = ''     

    #Checking rows
    if (theBoard['7'] == theBoard['8'] == theBoard['9'] == turn) or (theBoard['4'] == theBoard['5'] == theBoard['6'] == turn) or (theBoard['1'] == theBoard['2'] == theBoard['3'] == turn):
        winner = turn

    #Checking columns
    if (theBoard['7'] == theBoard['4'] == theBoard['1'] == turn) or (theBoard['8'] == theBoard['5'] == theBoard['2'] == turn) or (theBoard['9'] == theBoard['6'] == theBoard['3'] == turn):
        winner = turn

    #Checking diagonals
    if (theBoard['7'] == theBoard['5'] == theBoard['3'] == turn) or (theBoard['9'] == theBoard['5'] == theBoard['1'] == turn):
        winner = turn

    #No winner
    else:
        winner = ''

    return winner


def restartGame():
    choice = input("Play again? (y/n): ")
    if choice == 'y': 
        for values in theBoard:
            theBoard[values] = ' '
        clearScreen()
        main()
    else:
        print("Thank you for playing!")


#Main Function
def main():
    playGame()
    restartGame()


if __name__ == '__main__':
    main()


'''

7|8|9 
-+-+-
4|5|6
-+-+-
1|2|3

'''