def prime(n):
    a = 1
    b = 1
    while n % 2 == 0:
        if n % 2**2 == 0:
            a *= 2
            n //= 4
        else:
            b *= 2
            n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if n % (f**2) == 0:
                a *= f
                n //= f**2
            else:
                b *= f
                n //= f
        else:
            f += 2
    if n != 1:
        b *= n
    return a, b

n = int(input())
print(*prime(n))