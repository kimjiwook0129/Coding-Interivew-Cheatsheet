# https://www.acmicpc.net/problem/2110

if __name__ == "__main__":
    N, C = map(int, input().split())
    nums = []
    for _ in range(N):
        nums.append(int(input()))
    nums.sort()
    minDist, maxDist = 1, nums[-1] - nums[0]
    bestDist = minDist

    while maxDist >= minDist:
        cur, count = nums[0], 1
        mid = (maxDist + minDist) // 2

        for i in range(1, N):
            if cur + mid <= nums[i]:
                cur = nums[i]
                count += 1

        if count >= C:
            minDist = mid + 1
            bestDist = mid
        else:
            maxDist = mid - 1
    print(f"Result : {bestDist}")
