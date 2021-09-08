# 이것이 코딩테스트다 p.99

if __name__ == "__main__":
    N, K = map(int, input().split())
    result = 0
    while True:
        remainder = N % K
        result += remainder
        N -= remainder
        if N == 0:
            result -= 1
            break
        N //= K
        result += 1
    print(result)
