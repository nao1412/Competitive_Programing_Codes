x, y = map(int, input().split())

# a = [1,3,5,7,8,10,12]
# b = [4,6,9,11]
# c = [2]

# if (x in a and  y in a) or (x in b and y in b) or (x in c and y in c):
#   print('Yes')
# else:
#   print('No')

a = [0,1,3,1,2,1,2,1,1,2,1,2,1]
if a[x] == a[y]:
  print('Yes')
else:
  print('No')