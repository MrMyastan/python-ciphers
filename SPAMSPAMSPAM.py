import math

print('What would you like to say?')
text = input()
text = (text + ' ')

print('How many times?')
number = input()

if number == "max":
  numchar = len(text)
  number = 2000/numchar
  number = math.floor(number)

number = int(number)

finaltext=(text * number)


print(finaltext)