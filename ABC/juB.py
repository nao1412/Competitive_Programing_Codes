n = int(input())
r, b = [], []
for _ in range(n):
    x, c = input().split()
    if c == 'R':
        r.append(int(x))
    elif c == 'B':
        b.append(int(x))
r_s = sorted(r)
b_s = sorted(b)
# if r != []:
#     print('\n'.join(r_s))
# if b != []:
#     print('\n'.join(b_s))
for x in r_s:
    print(x)
for x in b_s:
    print(x)