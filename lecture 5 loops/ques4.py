#WAP to find factorial of first n numbers (using while loop)

fact, i = 1, 1
n = int(input("Enter number: "))

while i <= n:
    fact *= i
    i += 1
print(f"Factorial of first {n} numbers is {fact}")
