"""
MATCH CASE STATEMENT
A match-case statement is similar to a switch statement. We use a switch statement to transfer control to a particular block of code based on the value of the tested variable.

"""

#MATCH CASE STATEMENT syntax
# match variable_name:
#   case 'pattern_1':
#     //statement_1
#   case 'pattern_2':
#     //statement_2
#     .
#     .
#     .
#   case 'pattern_n':
#     //statement_N
x = int(input("Enter a value of X:"))
match x:
  case 0:
    print("X is zero")
  case 1:
    print("X is 1")
  #case with if Condition
  case _ if x > 1 and x <= 10:
    print("X is between 1 - 10")
  case _ if x > 10 and x <= 50:
    print("X is between 10 - 50")
  case _ if x > 50 and x <= 100:
    print("X is between 50 - 100")
  case x:
    print("X is above 100")