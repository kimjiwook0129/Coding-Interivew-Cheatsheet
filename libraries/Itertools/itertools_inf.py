import itertools

# Infinite Iterators

# Count
# Returns evenly spaced values starting with 'start'
for i in itertools.count(start=10, step=3):
    print(i, end=' ')  # 10 13 16 19 22
    if i > 20:
        print('')
        break

# Cycle
# Cycles through an iterator endlessly
for idx, elem in enumerate(itertools.cycle([1, 2, 3])):
    if idx > 7:
        print('')
        break
    print(elem, end=' ')  # 1 2 3 1 2 3 1 2

# Repeat
lst = [i for i in itertools.repeat(1, 7)]
print(lst)  # [1, 1, 1, 1, 1, 1, 1]
