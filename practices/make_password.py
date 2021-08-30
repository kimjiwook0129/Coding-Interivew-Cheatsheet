# https://www.acmicpc.net/problem/1759

from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']
if __name__ == "__main__":
    L, C = map(int, input().split())
    chars = list(input().split())
    chars.sort()
    for password in combinations(chars, L):
        vowels_count = len([p for p in password if p in vowels])
        if vowels_count >= 1 and L - vowels_count >= 2:
            print("".join(password))
