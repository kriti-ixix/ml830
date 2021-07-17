number = int(input("Enter a number: "))

if number%2 == 0:
    print("The number is even")
else:
    print("The number is odd")


age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible to vote")
elif age > 15 and age < 18:
    print("You are almost eligible to vote")
else:
    print("You are not eligible to vote")