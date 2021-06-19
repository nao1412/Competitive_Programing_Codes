s = str(input())
n = len(s)
t = []
for k in range(n):
    t.append(1)
for i in range(n):
    if s[i] == 'R':
        t[i] -= 1
        t[i+1] += 1
    elif s[i] == 'L':
        t[i] -= 1
        t[i-1] += 1
t =[str(a) for a in t]
t = ' '.join(t)
print(t)