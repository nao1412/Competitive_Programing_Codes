a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for x in range(n):
    b = int(input())
    for i in range(3):
        if a[0][i] == b