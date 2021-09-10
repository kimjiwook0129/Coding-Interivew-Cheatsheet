# 이것이 코딩테스트다 p.116
if __name__ == "__main__":
    data = input()
    col = ord(data[0]) - ord('a')
    row = int(data[1]) - 1
    drow = [-2, -2, -1, -1, 1, 1, 2, 2]
    dcol = [-1, 1, 2, -2, -2, 2, -1, 1]
    result = 0
    for i in range(8):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if nrow >= 0 and nrow < 8 and ncol >= 0 and ncol < 8:
            result += 1
    print(result)