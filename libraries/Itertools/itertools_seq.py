import itertools
import operator
from utils.itertools_printer import itertools_printer

# Sequential Iterators

data = [1, 2, 3, 4, 5]
# Accumulation
acc_mul = itertools.accumulate(data, operator.mul)
itertools_printer('Accumulation with mul', acc_mul)  # 1, 2, 6, 24, 120
acc_sum = itertools.accumulate(data)
itertools_printer('Default accumuation (sum)', acc_sum)   # 1, 3, 6, 10, 15

# Chain : Returns them as one long iterable
result = itertools.chain([1, 2, 3], [4, 5, 6])
itertools_printer('Chain', result)  # 1 2 3 4 5 6

# Compress
result = itertools.compress([1, 2, 3, 4], [True, False, True, False])
itertools_printer('Compress', result)  # 1 3

# Dropwhile : Drops while the predicate is true, returns afterwards
result = itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 1, 2])
itertools_printer('Dropwhile', result)  # 3, 4, 1, 2

# Filterfalse : Filter the ones that are false
result = itertools.filterfalse(lambda x: x < 3, [1, 2, 3, 4])
itertools_printer('Filterfalse', result)  # 3, 4

# Groupby : Groups things together
data = [
    {'name': 1, 'class': 'a'},
    {'name': 2, 'class': 'b'},
    {'name': 3, 'class': 'a'},
    {'name': 4, 'class': 'a'},
    {'name': 5, 'class': 'b'},
    {'name': 6, 'class': 'b'}
]
result = itertools.groupby(data, key=lambda x: x['class'])
for key, group in result:
    print(f'{key} : {list(group)}')
    # a: [{'name': 1, 'class': 'a'}]
    # b : [{'name': 2, 'class': 'b'}]
    # a : [{'name': 3, 'class': 'a'}, {'name': 4, 'class': 'a'}]
    # b : [{'name': 5, 'class': 'b'}, {'name': 6, 'class': 'b'}]

# Starmap
result = itertools.starmap(operator.mul, [(1, 3), (2, 6), (3, 7)])
itertools_printer('Starmap with *', result)  # 3 12 21
result = itertools.starmap(operator.sub, [(1, 3), (2, 6), (3, 7)])
itertools_printer('Starmap with -', result)  # -2 -4 -4

# Takewhile
result = itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])
itertools_printer("Takewhile", result)  # 1 2 3 4

# Tee : Returns n independent iterable from 1 iterable
original = [1, 2, 3]
a, b, c = itertools.tee(original, 3)
itertools_printer('Original', original)
itertools_printer('a', a)
itertools_printer('b', b)
itertools_printer('c', c)

# Zip_longest
arr1, arr2 = [1, 2, 3, 4, 5], [7, 8, 9]
result = itertools.zip_longest(arr1, arr2, fillvalue=None)
# 1, 7) (2, 8) (3, 9) (4, None) (5, None)
itertools_printer('Zip_longest', result)
