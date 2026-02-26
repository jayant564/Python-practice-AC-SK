#WAF print entered num is odd or even

def odd_even(x):
    if x == 0:  print("You entered 0")
    elif x%2==0: print("Even")
    else: print("Odd")

num = int(input("Enter number: "))

odd_even(num)
