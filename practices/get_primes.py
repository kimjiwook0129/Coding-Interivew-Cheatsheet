from math import sqrt
# https://www.acmicpc.net/problem/1929
# 아래토스테네스의 체 (Sieve of Eratosthenes)
if __name__ == "__main__":
    M, N = map(int, input().split())
    nums = [True for i in range(N + 1)]
    nums[1] = False
    for i in range(2, int(sqrt(N)) + 1):
        j = 2
        while i * j <= N:
            nums[i * j] = False
            j += 1
    for i in range(M, N + 1):
        if nums[i]:
            print(i)
