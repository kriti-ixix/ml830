myString = "Hi, how are you?"
myString2 = "I'm good!"

print(len(myString))
print(myString + " " + myString2) #String concatenation
print(myString * 5) #String multiplication

s1 = "Hello"

print(s1.lower())
print(s1.upper())

print(myString.split())

tweet = "Good morning! #niceweather #feelinggood #wow"
print(tweet.split("#"))
print(tweet.split("#", 1))

print(myString[0])
print(myString[5])

#String slicing
#string[start : stop : step]
print(myString[1:6])
print(myString[:10:2])
print(myString[::-1])