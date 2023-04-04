# string formatting
letter = "Hey my name is {} and I am from {}"
name = "Ishant"
country = "India"
print(letter.format(name, country))


price = 49.0273648
txt = f"For only {price:. 2f}"
print(txt)
