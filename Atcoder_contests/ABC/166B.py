import itertools

n, k = map(int, input().split())
d = [0]*k
a = []
for i in range(k):
    d[i] = int(input())
    sn = list(map(int, input().split()))
    a.append(sn)
res = itertools.chain(*a)
res = list(res)
res_s = list(set(res))
print(n - len(res_s))