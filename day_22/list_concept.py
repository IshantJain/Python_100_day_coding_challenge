#list 
"""
*** LIST ***
1. they are ordered collection of data items. 
2. they store multiple items in a single variable.
3. The items in list are seperated by commas ( , ) and enclosed in square brackets[].
4. they are changeable meaning we can alter them after creation.

index always starts with 0.
order maintain rahega
can have different data types in a list
negative indexing sould not perform normally always convert it to possitive indexing
"""

list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["red", "YELLOW", "Green"]

print(list1)
print(list2)
print(len(list1)-3)#negative index converted to possitive indexing.
"""
*** Finding a number in list ***
-> same thing applies in list as well.
"""
if 9 in list1:
  print("Yes")
else:
  print("No")

if "red" in list2:
  print("Yes")
else:
  print("No")

#-> String slicing
print(list1[1:6])
print(list1[1:8:2])#first do string slicing and then perform by skipping the number given at 3rd position in the syntax. 

print(list1[1:len(list1)-3]) # negative indexing done with string slicing

