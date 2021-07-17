'''
- Iterator
- Condition
- Increment/Decrement

Two types of loops: for and while -> Entry controlled loops
'''

i = 1 #Iterator

while i < 101: #Condition
    print(i)
    i += 1 #i = i + 1 Increment

i = 10

while i > 0:
    print(i)
    i -= 1


#range(start, stop, step)
#start = 0, stop is not included, step = 1

for x in range(10):
    print(x)

for x in range(10, -1, -1):
    print(x)

for number in range(101):
    if number%2 == 0 and number%3 == 0:
        print("x", number, sep=": ", end=", ")

message = "Hello world"

for char in message:
    if char != " ": 
        print(char)