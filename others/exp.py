with open('input.txt') as p:
    d = p.readlines()
f = []
m = int(d.pop(-1))
for i in d:
    e = i.split(':')
    f.append(e[0])
    f.append(e[1])
e_1 = [int(j) for j in f[::2]]
e_2 = [k for k in f[1::2]]  #ここをいじって改行コードを消す
e_22 = []
for r in e_2:
    r = r.strip()
    e_22.append(r)
# print(e_22)
g = dict(zip(e_22, e_1))
g_sorted = sorted(g.items(), key=lambda x:x[1])

print(len(g_sorted))