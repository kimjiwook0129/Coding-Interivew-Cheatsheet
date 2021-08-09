from timeit import default_timer
from test_harness import test_harness

# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3


def solution(test):
    N, stages = test['n'], test['stages']

    count, F_rates = [0] * (N + 2), [0] * N

    for stage in stages:  # Stage Count
        count[stage] += 1

    for i in range(N, 0, -1):  # Updating F_rates
        num = count[i]
        count[i] += count[i + 1]  # Count Accumulation
        den = count[i]
        F_rates[i - 1] = 0 if den == 0 else num / den  # F_rate

    F_rates = list(enumerate(F_rates))  # Indexing
    F_rates.sort(key=lambda x: -x[1])  # Sorting

    return [x[0] + 1 for x in F_rates]  # Return Index


if __name__ == "__main__":
    tests = [
        {"n": 5, 'stages': [2, 1, 2, 6, 2, 4, 3, 3], 'result':[3, 4, 2, 1, 5]},
        {"n": 4, 'stages': [4, 4, 4, 4, 4], 'result':[4, 1, 2, 3]},
    ]
    test_harness(solution, tests)
