n = int(input())
a = list(map(int, input().split()))
m = [0]*9
color = [0]*9
for i in a:
    if 1 <= i and i <= 399:
        m[0] = 1
        color[0] = 1
    elif 400 <= i and i <= 799:
        m[1] = 1
        color[1] = 1
    elif 800 <= i and i <= 1199:
        m[2] = 1
        color[2] = 1
    elif 1200 <= i and i <= 1599:
        m[3] = 1
        color[3] = 1
    elif 1600 <= i and i <= 1999:
        m[4] = 1
        color[4] = 1
    elif 2000 <= i and i <= 2399:
        m[5] = 1
        color[5] = 1
    elif 2400 <= i and i <= 2799:
        m[6] = 1
        color[6] = 1
    elif 2800 <= i and i <= 3199:
        m[7] = 1
        color[7] = 1
    else:
        color[8] += 1

print(max(sum(m),1), sum(color))