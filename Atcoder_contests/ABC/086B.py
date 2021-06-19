a, b = map(str, input().split())
c = int(a + b)

for i in range(4, 317):
    if i**2 == c:
        ans = 'Yes'
        break
    else:
        ans = 'No'

print(ans)