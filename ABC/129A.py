p, q, r = map(int, input().split())
ans = 0
if p <= q:
    a = p
    b = q
    if b <= r:
        ans = a + b
    else:
        ans = a + r
else:
    a = q
    b = p
    if b <= r:
        ans = a + b
    else:
        ans = a + r
print(ans)