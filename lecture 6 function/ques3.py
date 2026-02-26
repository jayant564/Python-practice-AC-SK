#WAF print the elements of list in single line

list = ["delhi", "noida", "gurgaon", "mumbai", "pune", "banglore"]

def print_list(a):
    for i in range(len(a)):
        print(a[i], end=" ")

print_list(list)
