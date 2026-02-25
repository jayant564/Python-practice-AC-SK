#WAP to find factorial of first n number (using for loop)

fact = 1
n = int(input("Enter number: "))

for i in range(1, n+1):
    fact *= i
print(f"Factorial of first {n} number is {fact}")
