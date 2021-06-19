s = str(input())
n = len(s)
t = []
for k in range(n):
    t.append(1)
for x in range(2):
    for i in range(n):
        if s[i] == 'R':
            if t[i] >= 1:
                t[i+1] = t[i]
                t[i] = 0       #全然違う
        elif s[i] == 'L':
            if t[i] >= 1:
                t[i-1] = t[i]
                t
t =[str(a) for a in t]
t = ' '.join(t)
print(t)