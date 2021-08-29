import math

# About O(N log N), it is more likely O(N loglog N)


def sieve_of_eratosthenes(num):
    check = [True for _ in range(num + 1)]

    for i in range(2, int(math.sqrt(num)) + 1):  # x0.5
        if check[i]:
            j = 2
            while num >= j * i:
                check[j * i] = False
                j += 1
    for i in range(2, n + 1):
        if check[i]:
            print(i, end=" ")
    print()


if __name__ == "__main__":
    n = int(input())
    sieve_of_eratosthenes(n)
