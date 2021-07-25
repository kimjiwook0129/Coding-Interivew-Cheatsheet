lst = [1, 2, 3, 4, 5]
for i, elem in enumerate(lst):  # List Enumerate
    print(f'index : {i}, element : {elem}')
    # index : 0, element : 1
    # ...
    # index : 4, element : 5

lst2 = [10, 20, 30, 40]
for a, b in zip(lst, lst2):  # Multiple List Zip
    print(a, b)  # Prints until the shorter list ends
    # 1 10
    # ...
    # 4 40

a, b, c = [1, 2, 3]  # Multiple Assignment

lst = [1, 3, 5, 7]

print(lst.index(5))  # 2 -> Returns the index

lst.append(9)  # append method
print(lst)  # [1, 3, 5, 7, 9]
lst.insert(1, 100)  # insert method
print(lst)  # [1, 100, 3, 5, 7, 9]

lst.sort(reverse=True)  # sorts the original list
sorted_lst = sorted(lst)  # returns a new list that is sorted

alphaLst = ['a', 'z', 'A', 'Z']
alphaLst.sort(key=str.lower)  # ['a', 'A', 'z', 'Z']
print(alphaLst)
