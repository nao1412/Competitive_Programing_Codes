s = int(input())
a = []
i = 1
ai = s
while ai not in a:
    a.append(ai)
    if ai % 2 == 0:
        ai //= 2
    else:
        ai *= 3
        ai += 1
    i += 1

print(i)