# ABC 151C
n, m = map(int, input().split())
ac = 0
wa = 0
cnt = [0]*n
for i in range(m):
    p, s = input().split()
    p = int(p)
    p -= 1
    if cnt[p] == -1:
        continue
    elif s == 'AC':
        ac += 1
        wa += cnt[p]
        cnt[p] = -1
    else:
        cnt[p] += 1
print(ac, wa)
