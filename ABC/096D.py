n = int(input())
prime5 = []
for i in range(1,5600):
  a = i * 10 + 1
  # flag = True
  for j in range(3,int(a**0.5) + 1):
    if a % j == 0:
      break
      # flag = False 使わないほうが速い
  else: prime5.append(a)
print(*prime5[:n])

N = int(input())
ans = []
x = 6
while len(ans) < N:
    for y in range(2, int(x**0.5)+1):
        if x % y == 0:
            break
    else:
        ans.append(x)
    x += 5
print(*ans)
