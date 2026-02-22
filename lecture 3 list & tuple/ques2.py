#WAP check if a list contains palindrome of element

list1 = [1, 2, 3, 2, 1]
list2 = list1.copy()

list2.reverse()

if list1 == list2:
    print("Yes Palindrome\n")
else:
    print("No\n")
