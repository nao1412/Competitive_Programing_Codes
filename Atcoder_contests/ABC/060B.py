a, mod, c = map(int, input().split())

for i in range(mod):
    if a*(i+1) % mod == c:
        print('YES')
        exit()
print('NO')