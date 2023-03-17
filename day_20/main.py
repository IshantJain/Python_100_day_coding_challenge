#FUNCTIONS
"""A function is a block of code that performs a specific task whenever it is called."""


#syntax = def(keyword) function_name(variable_1_name, variable_2_name)
def calculateGmean(a, b):
  mean = (a * b) / (a + b)
  print(mean)


i = 10
j = 10
calculateGmean(i, j)  #function called here with the variable name.

#function called
def isGreater(a, b):
  if (a > b):
    print("1st is greater")
  else:
    print("2nd is greater")


m = int(input("enter 1st number:"))
n = int(input("enter 2nd number:"))
isGreater(m, n)
