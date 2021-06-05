d_sorted = sorted(d.items(), key=lambda x:x[1])


m = d.pop(-1)
d.sort(reverse=False)
d_list = list(d.items())
print(d)

with open('input.txt') as p:
    d = p.readlines()
g = []
m = int(d.pop(-1))
for i in d:
    e = i.split(':')
    e_1 = [int(j) for j in e[::2]]
    e_2 = [k for k in e[1::2]]
    print(e_1)
g = dict(zip(e_1, e_2))

print(g)
print(m)