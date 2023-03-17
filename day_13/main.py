#String Methods
#There are some built in methods in python that can be used to modify and alter the string

#Strings are immutable

a = "Ishant Ishantt"
print(len(a))

#upper():
print(a.upper())
#lower():
print(a.lower())
#rstrip(): removes any trailing character.

print(a.rstrip("t"))

#replace(): replace all occurance of a string with another string.
print(a.replace("Ishant", "Ish"))
#replace the first string with the 2nd String passed in the arguments

#split(): it splits the given string at the specified istance and returns the separated string as list items.
print(a.split(" "))

#Capitalize(): Truns only the first character of the string to uppercase and the srest other remains lowercase.
heading = "introduction to python Day-13"
print(heading.capitalize())

#center(): method aligns the string to the center as per the parameters given by the user.
print(heading.center(50))

print(heading.capitalize().center(50)) #IMPORTANT
#here we have used both the functions hat are capitalize and center with 50 margin and we have performed bith the operations on the heading variable.

#Count(): method returns the number of times the given value has occured within the defined string
print(a.count("Ish"))

#endswith(): this method checks if the given string ends with a given character / value. If YES then return TRUE or else return FALSE. It will return boolean data type
print(a.endswith("t"))
#With this we can also check for a value in-between the string by providing satrt and end index position
#ISHANT
#print stmt (variable_name.endswith("character", starting index , ending index))
print(a.endswith("a", 2, 4)) 

#find(): this method searches for the first occurrence of the given value and returns the index where it is present.If the given value is absent from the string then return -1.
print(a.find("a"))
print(a.index("a"))


#isalnum(): method returns TRUE only if the entire string only consists of A_Z a_z 0-9. If we have any character like alphabets or numbers no puncuations or symbols.












