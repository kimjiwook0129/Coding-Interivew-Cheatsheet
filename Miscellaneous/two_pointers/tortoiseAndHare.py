

def tortoiseAndHare(lst):
    first, second = lst[0], lst[0]
    while True:
        first = lst[first]
        second = lst[lst[second]]
        if first == second:
            break
    first = lst[0]
    while first != second:
        first = lst[first]
        second = lst[second]
    return first

if __name__ == "__main__":
    lst = [8, 3, 2, 4, 5, 6, 1, 4, 7]
    print(tortoiseAndHare(lst)) # 4