"""
  ***  tuples  ***
-> Tuples are immutable and list are mutable.
  
-> In tuples we can not change the values present inside the tules.

-> The main difference between the list and the tuple is that we can not change the values of the tuple but we can change the values of the list.

-> All the concepts are the same as that of the list.

"""
tup = (1, 5, 6, 7, 8)  #tuple created.
print(type(tup), tup)
print(tup[2]) #tupel indexing it will print the value present at the particular index.

#checking for the item presnt in the tuple.
if 5 in tup:
  print("Yes 5 is present in the tuple.")
else:
  print("No it is not present")


#tuple slicing: for this we have to create a new tuple and store and print that new tuple.
tup2 = tup[1:3 ]#staring from 1 till 3rd index it will stroe in the new tuple.





