#WAP to find sum of first n numbers (using for loop)

sum = 0
n = int(input("Enter number: "))

for i in range(1, n+1):
    sum += i
print(f"Sum of first {n} number is {sum}")
