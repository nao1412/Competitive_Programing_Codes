d, n = map(int, input().split())

if n < 100:
    print(n * 100**d)
else:
    print(101 * 100**d)