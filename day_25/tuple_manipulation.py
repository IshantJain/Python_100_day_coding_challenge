"""
    *** Manipulating Tuple ***

-> tuples  are immutable and if we want to add, remove, change tuple items then first we have to convert the tuple into a list. then we will perform the operations on the converted list and then convert it back to tuple.

"""

# tuple created -> then converted to list -> actions performed on the list -> then again converted to tuple -> and then rint it.

color = ("Red", "Yellow", "Green", "Blue", "Orange")
temp = list(color)
temp.append("White")  #adding an item.
temp.pop(4)  #remove item.
temp[3] = "Pink"  #change item.
color = tuple(temp)
print(color)

# tuple concatenation
# we can directly concatenate 2 tuple and insert them into the 3rd one.
name1 = ("Ishant", "Madan", "Naveen", "Dibyendu")
name2 = ("Shiavnshu", "Satyam", "Saurav", "Nikhil")
name_008 = name1 + name2
print(name_008)

#tuple method
"""count():  it returns the number of time an element has occured in the tuple."""
tuple1 = (0, 1, 5, 3, 4, 5, 6, 7, 8, 5)
res = tuple1.count(5)
print("count of 5 in tuple1 is:", res)
"""index(): returns the first occurance of the value in the tuple. """
tuple1 = (0, 1, 5, 3, 4, 5, 6, 7, 8, 5)
res = tuple1.index(5)  #for 1st occurance in the tuple.
res1 = tuple1.index(  5, 4, 9)  # here it will first slice the tuple from 4th to 9th place and then it will find 5's 1st occurance.
print("count of 5 in tuple1 is:", res)
res = len(tuple1)  #to get the length of the tuple.
print(res)