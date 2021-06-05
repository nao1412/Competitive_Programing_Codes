n = int(input())
for i in range(8):
    if n >= 2**i:
        ans = 2**i
print(ans)
