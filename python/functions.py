'''
Four types of functions:
On the basis of parameters: Default method, Parameterised method
On the basis of return type: No return type, Return type
'''


def addNumbers(): #Default method
    first = int(input("First number: "))
    second = int(input("Second number: "))
    print("Sum is", first + second)
 
def subNumbers(a, b): #Parameterised method
    print("Difference is", a - b)

def multiplyNumbers(a, b, c):
    return a * b


addNumbers()
subNumbers(10, 20)
product = multiplyNumbers(200, 300, 100)
product2 = multiplyNumbers(50, 50, 60)

print("Products are", product, product2)