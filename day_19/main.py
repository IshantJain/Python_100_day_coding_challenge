# BREAK AND CONTINUE STATEMENT
"""  
***  Break Statement  ***
it enables a programe to skip over a part of the code. A break statement terminates the very loop it is in.

Breaking out of the loop.

continue statement refers to skipping the particular iteration and the again continue the loop.
"""
for i in range(13):
  if (i == 9):
    print("Skip the 9th iteration")
    continue
  print("5 X", i, "=", 5 * i)
