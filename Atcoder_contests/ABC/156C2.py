n = int(input())
x = list(map(int, input().split()))
ans1 = 0
ans2 = 0
xa = sum(x) // n
for i in x:
    ans1 += (abs(i-xa))**2

for i in x:
    ans2 += (abs(i-xa-1))**2

print(min(ans1, ans2))
