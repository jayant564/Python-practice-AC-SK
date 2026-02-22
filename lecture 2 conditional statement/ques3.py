#WAP check if number is a multiple of 7 or not

x = int(input("Enter number: "))

if x==0:
    print("You entered 0\n")
elif x%7==0:
    print(f"{x} is multiple of 7\n")
else:
    print(f"{x} is not a multiple of 7\n")
