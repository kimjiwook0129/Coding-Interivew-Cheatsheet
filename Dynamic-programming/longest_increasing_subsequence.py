# Longest Increasing Subsequence

if __name__ == "__main__":
    array = [1, 2, 1, 3, 2, 5]
    dp = [1] * len(array)
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp[-1])
