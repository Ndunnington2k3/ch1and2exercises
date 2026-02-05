#Excercise 1
print(round(42.5))
print(round(42.6))
print(round(43.5))
print("python rounds .5's to the nearest even number, either up or down.")

#Exercise 2
print(2++2)
print(2+-2)
print("If one of the parentheses is left out, it's a syntax error.")\

#Exercise 3
print(type(175))
print(type(2.178))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs))
print(type(int))
print(type(type))

#Exercise 4. Wanted to do this one with only techniques from ch1 but it got too messy.
#My apologies for falling behind.
seconds = 42*60+42
print(seconds)
miles = 10/1.61
print(miles)
secspermile = seconds/miles
print(secspermile)

minutes = int(seconds//60)
seondsadd = int(seconds%60)
print(minutes, "minutes", seondsadd, "seconds per mile")

hours = minutes/60
speed_mph = miles/hours
print(speed_mph,"miles per hour")