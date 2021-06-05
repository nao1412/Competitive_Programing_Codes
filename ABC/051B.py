k, s = map(int, input().split())
ans = 0
for x in range(min(k, s) + 1):
    for y in range(min(k, s-x) + 1):
        z = s - x - y
        if z < 0 or z > k:
            continue
        ans += 1
print(ans)