#WAF to conver USD to INR

def curr_conv(a):
    return a *(91.06)

x = int(input("Enter how many dollars you have: "))

print(f"{x} USD is {curr_conv(x)} INR")
