n, q = map(int, input().split())
s = input()
l, r = [0]*q, [0]*q
for i in range(q):
    l[i], r[i] = map(int, input().split())

cs = [0]*(n+1)
for i in range(n):
    if i+1 < n and s[i] == 'A' and s[i+1] == 'C':
        cs[i+1] = cs[i] + 1
    else:
        cs[i+1] = cs[i]

for i in range(q):
    print(cs[r[i]-1] - cs[l[i]-1])
