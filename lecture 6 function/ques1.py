#Function to print average of 3 numbers

def cal_avg(a,b,c):
    return (a+b+c)/3

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

print(cal_avg(num1, num2, num3))