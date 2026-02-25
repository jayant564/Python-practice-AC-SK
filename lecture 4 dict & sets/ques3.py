'''WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary and add one by one.
Use subject name as key and marks as value.'''

marks = {}

x = int(input("Enter Physics marks: "))
marks.update({"Phy" : x})

x = int(input("Enter Chemistry marks: "))
marks.update({"Chem" : x})

x = int(input("Enter Maths marks: "))
marks.update({"Maths" : x})

print(marks)
