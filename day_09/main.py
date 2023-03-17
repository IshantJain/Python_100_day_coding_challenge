#TYPE CASTING
'''The conversion of one data type into another data type is called type casting in python or type conversion in python. 

Python supports a wide range of functions or methods like : 
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.... for type cassting in python. 
'''
'''
There are two types of type casting:
1. Explicit Conversion (Done by Us)
2. Implicit Conversion (Done by python itself automatically)
'''
#1. Explicit Conversion (Done by Us)
a = "1"
b = "2"
#TypeCasting done by us.
print (int(a) + int(b))

#2. Implicit Conversion (Done by python itself automatically)
c = 1.5
d = 2
#TypeCasting done automatically by python  conveting higher dataType to lower dataType
print (c + d)
