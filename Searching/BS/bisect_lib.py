from bisect import bisect_left, bisect_right
# Each function peforms at O(log N)
a = [1, 2, 4, 4, 4, 4, 7, 8, 8]
x = 0

print(f'First index to place x in a {bisect_left(a, x)}')  # 2
print(f'Last index to place x in a {bisect_right(a, x)}')  # 4
