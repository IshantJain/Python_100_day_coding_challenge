"""
***  Recursion  ***
Recursion is the process of defining something in terms of itself.  

"""


#factorial of a number
# factorial(5) = 5*4*3*2*1
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(3))


# Fibonacci Sequence
def fibonacci(n):
  if (n < 0):
    print("Enter a valid input")

  elif (n == 0 or n == 1):
    return 0 or 1

  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(4))
