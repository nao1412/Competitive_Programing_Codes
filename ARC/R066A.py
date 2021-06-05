n = int(input())
a = list(map(int, input().split()))
d = 0

if n % 2 == 0:
    for i in range(n//2):
        d += (2*i + 1) * 2
    if d != sum(a):
        print(0)
        exit()
else:    
    for i in range(1, n//2+1):
        d += 4 * i
    if d != sum(a):
        print(0)
        exit()

print(2**(n//2) % (10**9+7))