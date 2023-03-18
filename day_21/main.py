#function arguments and return statements
def average(a, b):
  print("the average is", (a+b)/2 ) 

average(10,5)

#Function arguments and return statement
"""
there are 4 types of arguments that we can provide in a function:

1. Default Args
2. Keyword Args
3. Variable length Args
4. Required Args

"""

"""
*** Default Argument ***

We provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument. 
* we change the order of the arguments as well as the order can not matter when we use the syntax like :
name(fname="is",mname="ha",lname="nt") #can be in any order.

"""
 
def name(fname, mname = "Ishant", lname = "Aunchaliya"):
  print("Hello",fname,mname,lname)

name("Ishant")

#Required argument
"""
if we dont pass the argument with a key=value syntax, then we have to pass the arguments in the correct positional order. like:
name(fname="is",mname="ha",lname="nt") #same order

"""
def average(*number):#here we have used *number so that we can make the number variable as a tuple.
  sum = 10
  for i in number:
    sum = sum + i
  print("average is: ", sum/len(number))
average(100, 100)  


def addition(*number):#here we have used *number so that we can make the number variable as a tuple.
  sum = 0
  for i in number:
    sum = sum + i
  return sum # it is used to return the value of the expression back to the calling function.
  # print("addition is: ", sum)
  
a = addition(100, 100)  
print(a)




