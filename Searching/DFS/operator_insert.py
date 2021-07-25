# n number of A1, ..., An numbers are provided
# n - 1 number of operators are provided
# Ignore operators priority, just do it in order
# Division -> int(num / divisor)
# Do not change the order of the numbers provided, only change the ops order

# First Line : 2 <= n <= 11
# Second Lin : 1 <= A1, ..., An <= 100
# Third line : a b c d where a, b, c, d = # of +, -, *, /
# Print the max & min results
# -1billion <= max, min <= 1billion

# https://www.acmicpc.net/problem/14888

from itertools import permutations, accumulate, product
import timeit


def solution1(n, nums, ops):  # DFS
    global largest, smallest

    def dfs(idx, cur_num):
        global largest, smallest, ops
        if idx >= n:
            largest = max(largest, cur_num)
            smallest = min(smallest, cur_num)
            return
        if ops[0] > 0:
            ops[0] -= 1
            dfs(idx + 1, cur_num + nums[idx])
            ops[0] += 1
        if ops[1] > 0:
            ops[1] -= 1
            dfs(idx + 1, cur_num - nums[idx])
            ops[1] += 1
        if ops[2] > 0:
            ops[2] -= 1
            dfs(idx + 1, cur_num * nums[idx])
            ops[2] += 1
        if ops[3] > 0:
            ops[3] -= 1
            dfs(idx + 1, int(cur_num / nums[idx]))
            ops[3] += 1

    dfs(1, nums[0])


def solution2(n, nums, ops):  # itertools.product
    global largest, smallest
    for each in list(product(['+', '-', '*', '/'], repeat=n-1)):  # O(4^(n-1)) ≈ O(4^n)
        cur = nums[0]
        add, sub, mul, div = ops
        for idx, op in enumerate(each):  # O(n)
            if op == '+':
                add -= 1
                cur += nums[idx + 1]
            elif op == '-':
                sub -= 1
                cur -= nums[idx + 1]
            elif op == '*':
                mul -= 1
                cur *= nums[idx + 1]
            else:
                div -= 1
                cur = int(cur / nums[idx + 1])
            if add < 0 or sub < 0 or mul < 0 or div < 0:
                break
        else:
            largest = max(largest, cur)
            smallest = min(smallest, cur)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))  # +, -, *, /
    print('Which solution? (1/2 : DFS/Itertools.product) :', end=' ')
    solution_num = input()
    start = timeit.default_timer()
    largest, smallest = -1e9, 1e9
    if solution_num == '1':
        solution1(n, nums, ops)
    else:
        solution2(n, nums, ops)

    print(largest)
    print(smallest)
    end = timeit.default_timer()
    print(f'Time Elasped : {end - start}s')
