
# Best # of coins to give change using changes given to make n
n = int(input())
count = 0
changes = [500, 100, 50, 10]
for change in changes:
    count += n // change
    n %= change
print(count)
