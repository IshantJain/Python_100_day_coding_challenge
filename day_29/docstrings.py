#Docstrings in python
"""
docstrings are the string literals that appear right after the definition of a function, method, class or module.

-> it neeeds to be right below the function name or below the class declaration.
"""
def square(n):
   '''Take a number n, returns the square of n'''
  print(n**2)
square(5)
print(sqaure.__doc__)