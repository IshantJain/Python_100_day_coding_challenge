#decision making with PYTHON using ifElse, elif, else stmts
#CONDITIONAL OPERATORS
# < , > , <= ,>= , == , !=

#if else
a = int(input("Enter your age: "))
print("Your age is ", a)
if (a > 18):
  print("You can drive")
else:
  print("You can not drive car")

#elif statement
num = int(input("Enter the value of num:"))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is zero.")
else:
  print("Number is poaitive.")

#Nested if statement

num = int(input("Enter the value of num:"))
if (num < 0):
  print("Number is negative.")

elif (num == 0):
  print("Number is zero.")

else:
  print("Number is positive.")
  if (num > 0 and num <= 10):
    print("number is between 0 and 10")
  elif (num < 10 and num <= 20):
    print("Number is btwn 10 and 20")
  else:
    print("number is above 20.")
