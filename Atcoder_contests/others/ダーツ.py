n, m = map(int, input().split())
ans = 0
for _ in range(n):
    a = list(int(input()))
a_s = a.sort(reverse=True)
while ans < m:
    ans += #同じ値を使うことができる