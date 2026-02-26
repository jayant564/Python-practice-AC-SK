#WAF to calculate sum of first n natural numbers using recursion

def cal_sum(n):
    if n==0:
        return 0
    return n + cal_sum(n-1)

num = int(input("Enter number: "))

print(cal_sum(num))
