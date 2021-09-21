# 이것이 코딩테스트다  p.182

import sys

if __name__ == "__main__":
    N, K = map(int, input().split())
    lst_A = list(map(int, sys.stdin.readline().rstrip().split()))
    lst_B = list(map(int, sys.stdin.readline().rstrip().split()))
    lst_A.sort()
    lst_B.sort()
    for i in range(K):
        a = lst_A[i]
        b = lst_B[N - i - 1]
        if b > a:
            lst_A[i], lst_B[N - i - 1] = b, a
        else: 
            break
    print(sum(lst_A))