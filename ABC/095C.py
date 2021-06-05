a, b, c, x, y = map(int, input().split())

k = []
for i in range(10**5+1):
    plc = 2*c*i + max(x-i,0)*a + max(y-i,0)*b
    k.append(plc)

print(min(k))