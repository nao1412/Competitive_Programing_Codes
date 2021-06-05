n = int(input())

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]
for i in a:
  for j in b:
    if i * j == n:
      print('Yes')
      exit()
print('No')