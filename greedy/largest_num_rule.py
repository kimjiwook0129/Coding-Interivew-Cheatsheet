# N, M, K : N # of numbers, add M times to make the largest num, cannot add the same number K times consecutive
# input)
# 5 8 3
# 2 4 5 4 6
# output)
# 46
# since 6 + 6 + 6+ 5 + 6 +6 +6 +5 = 46
if __name__ == "__main__":
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    full_cycle = M // (K + 1)
    final = full_cycle * nums[1] + (M - full_cycle) * nums[0]
    print(final)
