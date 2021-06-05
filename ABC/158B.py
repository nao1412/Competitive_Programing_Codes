n, a, b = map(int, input().split())

x = n // (a+b)
if n%(a+b) <= a:
    print(x*a + n%(a+b))
elif n%(a+b) > a:
    print((x+1) * a)
else:
    print(x*a)