#while loop it executes statements while the condition is true.When the condition becomes false it comes out of the loop.
#Incrementing Loop
#
# i = 0
# while (i <= 3):
#   i = int(input("Enter a number:"))
#   print(i)
#   i = i + 1

#Decrementing loop and using ELSE with it
# i = 5
# while (i >= 0):
#   print(i)
#   i = i - 1
# else:
#   print("Hello World")
"""*  Interview Question  *"""
'''EMULATED do while loop 
The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true.'''
while True:
  i = int(input("Enter a number:"))
  print(i)
  #here it will change the condition from true to false and create a infinite looping system.
  if not i < 100:
    break
