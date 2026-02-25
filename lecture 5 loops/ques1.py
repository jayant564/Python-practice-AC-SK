#WAP to find sum of first n numbers (using while loop)

sum, i = 0, 1
n = int(input("Enter number: "))

while i <= n:
    sum += i
    i += 1
print(f"Sum of first {n} numbers is {sum}")
