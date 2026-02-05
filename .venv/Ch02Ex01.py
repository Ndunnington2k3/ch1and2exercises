#Exercise 1
print("17 = n is not correct. Syntax Error.")
n = 17
#This sets n up as a variable that = 17
print(n)
#17

x = y = 1
#Surprisingly this works. Could be used in interesting ways.
print(x, y);
#Semicolon works. period does not.
#importing 'maath' is invalid because maath is not a library.
#I could make 'maath.py' and import that, though.
import math

#Exercise 2
#Pt1:
r = 5
vol = (4/3)/(math.pi * r **3)
print(vol, "is the volume of the sphere")

#Pt2:
varx = 42
print((math.cos(varx) ** 2) + (math.sin(varx) ** 2), "still equals 1")

#Pt3:
print(math.e ** 2)
print(math.pow(math.e, 2))
print(math.exp(2))
print("There are many ways to get the same result. I wonder which is most efficient?")
print("If I had to guess, the first and third are fastest compared to the second.")
