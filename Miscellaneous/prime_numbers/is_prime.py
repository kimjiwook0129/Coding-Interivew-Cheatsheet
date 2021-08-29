import math

# O(X^0.5)


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    result = is_prime(n)
    if result:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
