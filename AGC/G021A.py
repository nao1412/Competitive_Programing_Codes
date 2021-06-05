n = int(input())

if n < 10:
    print(n)
else:
    n = str(n)
    l = len(n)
    if n == n[0] + '9'*(l-1):
        print(int(n[0]) + 9 * (l-1))
    else:
        print(int(n[0]) + 9*(l-1) -1)
