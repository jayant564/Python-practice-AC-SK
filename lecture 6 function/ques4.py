#WAF find the factorial of n

def find_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"Factorial of {n} is {fact}")

num = int(input("Enter number: "))

find_fact(num)