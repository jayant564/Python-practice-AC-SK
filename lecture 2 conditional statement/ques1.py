#WAP check if number entered by user is odd or even

num = int(input("Enter number: "))

if num==0:
    print(f"Number = 0\n")
elif num%2==0:
    print("Even\n")
else:
    print("Odd\n")
