n = int(input())
s = str(input())
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in s:
    print(a[(a.index(i) + n) % 26], end = '')
