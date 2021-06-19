n = int(input())
s = input()

num = [0,1,2,3,4,5,6,7,8,9]
memo = []
for i in num:
  for j in num:
    for k in num:
      memo.append(str(num[i]) + str(num[j]) + str(num[k]))

ans = 0

for i in memo:
  x = 0
  for j in range(n):
    if i[x] == s[j]:
      x += 1
      if x == 3:
        break
  if x == 3:
    ans += 1
    
print(ans)