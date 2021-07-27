from bisect import bisect_left, bisect_right
# Each function peforms at O(log N)
a = [1, 2, 4, 4, 8]
x = 4

print(f'First index to place x in a {bisect_left(a, x)}')
print(f'Last index to place x in a {bisect_right(a, x)}')
