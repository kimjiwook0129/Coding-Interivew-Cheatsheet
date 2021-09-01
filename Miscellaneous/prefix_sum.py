n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    prefix_sum.append(i + prefix_sum[-1])
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
