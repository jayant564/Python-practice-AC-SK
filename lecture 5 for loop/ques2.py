# Search for a number x in this tuple using loop 
# [1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter number to search: "))

idx = 0         # cannot print index directly
for i in nums:
    if x == i:
        print(f"{x} found at index {nums[idx]}\n")
idx += 1
