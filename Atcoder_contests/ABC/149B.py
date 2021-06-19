a, b, k = map(int, input().split())
if a < k <= a+b:
    b -= k-a
    a = 0
elif a >= k:
    a -= k
else:
    a = 0
    b = 0
print(a, b)