# 이것이 코딩테스트다 p.180

if __name__ == "__main__":
    N = int(input())
    students = []
    for _  in range(N):
        score_info = input().split()
        name, score = score_info[0], int(score_info[1])
        students.append((name, score))

    students.sort(key = lambda x: x[1], reverse=False)
    for student in students:
        name = student[0]
        print(name, end=' ')
    print()