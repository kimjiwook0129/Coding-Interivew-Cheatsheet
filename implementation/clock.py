# 이것이 코딩테스트다 p.113
# 00:00:00 ~ N:59:59 at least one 3 is included

if __name__ == "__main__":
    N = int(input())

    ### Method 1 ###
    sec_in_min, min_in_hour = 60, 60
    instances_in_60 = 0
    for i in range(60):
        if '3' in str(i):
            instances_in_60 += 1
    result = 0
    hour = 0  # 3, 13, 23
    while N >= hour:
        if hour == 3 or hour == 13 or hour == 23:
            result += 3600
        else:
            result += instances_in_60 * 60
            result += (60 - instances_in_60) * instances_in_60
        hour += 1
    print(result)

    ### Method 2 ###
    result = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    result += 1
    print(result)
