n = int(input())
s, t = map(str, input().split())
d = ''
for i in range(n):
    d += s[i] + t[i]
print(d)