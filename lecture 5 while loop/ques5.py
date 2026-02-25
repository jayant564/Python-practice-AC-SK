# Search for a number x in this tuple using loop 
# [1,4,9,16,25,36,49,64,81,100]

num = (1,4,9,16,25,36,49,64,81,100)
idx = 0
x = int(input("Enter number to search: "))
while idx < len(num):
    if num[idx] == x:
        print(f"{x} found at index {idx}")
    idx += 1
