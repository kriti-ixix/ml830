try:
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    if length < 0 or breadth < 0:
        raise ValueError

    print("The area is", length * breadth)

except:
    print("Length and breadth cannot be negative")