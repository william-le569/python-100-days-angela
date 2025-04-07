a = [[1, 2], [3, 4]]  # original list of lists
b = a[:]              # shallow copy of a
print("a:", a)
print("b:", b)
a[0][0] = 99          # modify the first element of the first inner list
print("a:", a)
print("b:", b)

a = [1, [3, 4]]  # original list of lists
b = a[:]              # shallow copy of a
print("a:", a)
print("b:", b)
a[0] = 99
a[1][0] = 99          # modify the first element of the first inner list
print("a:", a)
print("b:", b)