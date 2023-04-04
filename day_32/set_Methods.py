"""
  ***  SET METHODS  ***
- collection of welldefined objects.

JOINING SETS
i. union() and update()

- union() prints all the items that are present in all the joining sets.

- update() will update one of the set with all the items of the other set.

"""
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(
  s2))  #union items of both the sets will be printed without duplicate item.

s1.update(
  s2)  #it will add the values of the s2 in s1 without repeating the valuies
print(s1, s2)
"""
Intersection and intersection_update

- Common items in both the sets will not get printed when used intersection.
- order doesnot matter.
- only those values will get intersected which are there in both of the sets.

- 
"""
city1 = {"Jodhpur", "Jaipur", "Bengaluru", "Hyd", "Hubli", "Indore"}
city2 = {"Hyd", "Hubli", "Jaipur", "Indore"}
city3 = city1.intersection(city2)
city4 = city1.intersection_update(city2)
print(city3)
print(city4)

#To add something in a set we can use the add function
city5 = {"Jodhpur", "Jaipur", "Bengaluru", "Hyd", "Hubli", "Indore"}
city5.add("Pune")
print(city5)
#we can use update function/method to add values in the set.
city5.update("Rj")
#to remove()/discard() an item from list of the set.
city5.remove("Rj")
#main difference between remove and discard is that when we use remove and that item is not present in the set then it will rasie an error but discard() method will not raise error.
city5.discard("Delhi")

 #pop(): this method removes the last item from the list of the set but the catch is that which item is removed we dont know coz the list is unordered but we can check which item is being removed or poped out.
item = city5.pop()
print(item)
print(city5)










