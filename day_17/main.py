#LOOPS
#for loop
"""it can iterate over a sequence of iterable objects in python Iterating over a sequence is nothing but iterating over string , list , tuples, sets and dictionaries"""
#iterating over a string:
name = "Ishant"
for i in name:
  print(i, end=" , ")
  # if (i == "Ish"):
  #   print("ishant")

#iterating over a list:
colors = ["red", "Green", "Blue", "White"]
for x in colors:
  print(x)
  for i in x:
    print(i)

#range():

for k in range(5):
  print(k)

#when run with single argument then it will run from 0 to n-1
#and we can put k+1 to print till the given range number.
for j in range(1, 10, 2):
  print(j)
#in this it will skip 2 number and print other like 1, 3, 5, 7, 9 till the 2nd argument given in the range.
