first = [1, 2, 3, 4]
# second = []

# for x in first:
#     second.append(x**2)

second = [x**2 for x in first]
print(second)

even = [x**2 for x in first if x**2%2 == 0]
print(even)