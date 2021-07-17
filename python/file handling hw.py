choice = input("Make a choice:\n1.Read notes\t2.Write notes\nYour choice: ")

if choice == 'r':
    notes = open('notes.txt', 'r')
    print(notes.read())
    notes.close()

elif choice == 'w':
    numberOfNotes = int(input("How many notes do you want to write? "))
    notes = open('notes.txt', 'w')

    for i in range(1, numberOfNotes+1):
        note = input("Enter Note " + str(i) + ": ")
        notes.write("Note " + str(i) + ": " + note + "\n")
    
    notes.close()

else:
    print("The input was invalid")
