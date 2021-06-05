s = input()
n = len(s)

a = '0'
b = '1'
for i in range(1,n):
    if a[i-1] == '0':
        a += '1'
    else:
        a += '0'
for i in range(1,n):
    if b[i-1] == '0':
        b += '1'
    else:
        b += '0'

ca, cb = 0, 0
for i in range(n):
    if a[i] != s[i]:
        ca += 1
    if b[i] != s[i]:
        cb += 1

print(min(ca,cb))