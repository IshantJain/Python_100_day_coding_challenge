#Sets
"""
  *** SETS ***
- sets are UNORDERED collection of data items.

- it stores multiple items in a single variable.

- they are seperated by commas and enclosed          within {}.

-It does not maintain an order it can be             displayed in a shuffeled/random order, so that    is why they can not be accessed using the         index numbers.

- items of sets cannot be changed once created.

- sets do not contains duplicate items.

- it is a collection of well defined objects.


"""
x  =  {1,2,3,3,2,1}#set created.
print(x)#all the values will be printed only once.

empty_set  =  {} #this will create an empty dict.
set_empty  =  set()#this will create an empty set.
print(type(empty_set))
print(type(set_empty))

i = {3,2,1,7,3,892,4,312,2}
for y in i:
  print(y)
