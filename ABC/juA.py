#juA
s, l, r = map(int, input().split())
if s <= l:
    print(l)
elif s > l and s < r:
    print(s)
else:
    print(r)