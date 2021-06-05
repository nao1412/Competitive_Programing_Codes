n = int(input())
sp = []
for i in range(n):
    sspp = list(map(str, input().split()))
    sspp[1] = int(sspp[1])
    sspp.append(i+1)
    sp.append(sspp)

# sp.sort(key=lambda x: x[0])
sp.sort(key=lambda x: (x[0], -x[1]))

for i in range(n):
    print(sp[i][2])