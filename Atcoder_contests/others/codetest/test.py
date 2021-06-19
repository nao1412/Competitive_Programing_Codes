with open('input.txt') as p:
    d = p.readlines()
f = []
m = int(d.pop(-1))
for i in d:
    e = i.split(':')
    f.append(e[0])
    f.append(e[1])
e_1 = [int(j) for j in f[::2]]
e_2 = [k for k in f[1::2]]        
e_22 = []
for r in e_2:
    r = r.strip()
    e_22.append(r)
g = dict(zip(e_22, e_1))
g_sorted = sorted(g.items(), key=lambda x:x[1])

ans = ''
cnt = 0
for z in range(len(g_sorted)):
    y = g_sorted[z][1]
    if m % y == 0:
        ans += g_sorted[z][0]
        cnt += 1
if cnt == 0:
    print(m)
else:
    print(ans)

#pfXvTAYBYjEAuamAEasFqMSrwrRSN6