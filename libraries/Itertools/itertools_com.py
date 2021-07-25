import itertools
from utils.itertools_printer import itertools_printer

# Combinatoric Iterators

data = [1, 2, 3]
# Product
result = itertools.product(data, repeat=2)
# (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)
itertools_printer('Product', result)

# Combination
result = itertools.combinations(data, 2)
itertools_printer('Combination', result)  # (1, 2) (1, 3) (2, 3)

# Permutations
result = itertools.permutations(data)
# (1, 2, 3) (1, 3, 2) (2, 1, 3) (2, 3, 1) (3, 1, 2) (3, 2, 1)
itertools_printer('Permutation', result)

# Combinations with Replacement
result = itertools.combinations_with_replacement(data, 2)
# (1, 1) (1, 2) (1, 3) (2, 2) (2, 3) (3, 3)
itertools_printer('Combinations with Replacement', result)
