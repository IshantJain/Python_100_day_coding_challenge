"""
***  LIST METHODS  ***


list.append("value")
this function will then update the list with the value which is given in the value space but only while displaying. 
#Syntax: list_name.append("value_we_want_to_give")
"""
#list_appended
list1 = [2, 6, 1, 7, 3, 8, 4]
print(list1)
list1.append(5)
print(list1)
"""
list.sort()
this method sorts the list in ascending order.
the original list is updated.

"""
list1.sort()  #for ascending order.
print(list1)
list1.sort(reverse=True)  #for descending order.
print(list1)
list1.reverse()  #it will reverse the original list.
print(list1)
print(list1.index(5))  # it will give the indexing value of the given variable.
print(list1.count(5))  # it will count the occurance of the value passed.

#copy method
list2 = list1.copy(
)  #here it will copy the content of the list1 in the lis2 and perform all the edits and changes on the list2.
list2[0] = 0
print(list2)

#insert()
list1.insert(
  1, 10
)  # the first value passed is the index number where we want to insert a new value and after comma the new value what we want to insert is passed.

#extend()
list3 = [100, 110, 120]
list1.extend(list3)#list3 kholo list1 mei add kar do that is extend kar do list1 ko.
print(list1)

#concatinating two_list
list4 = list1 + list3 #here lsit1 and list3 will get combined and stored in list4.



