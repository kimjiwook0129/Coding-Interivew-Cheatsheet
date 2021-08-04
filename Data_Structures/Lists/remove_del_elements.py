lst = [1, 2, 3, 4, 5]
lst.remove(2)  # removes only the first instance
# remove causes error when cannot find the given element
# be aware of the error when using 'remove()'

print(lst)  # [1, 3, 4, 5]
del lst[1]
print(lst)  # [1, 4, 5]

a = lst.pop(0)  # Pops the first element
print(a)  # 1
b = lst.pop()  # Pops the last element
print(b)  # 5
