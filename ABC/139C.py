#ABC 139C
n = int(input())
h = list(map(int, input().split()))
cnt = 0
move_cnt = []
for i in range(n-1):
   if h[i] >= h[i+1]:
      cnt += 1
      move_cnt.append(cnt)
   else:
      cnt = 0
      move_cnt.append(cnt) 
print(max(move_cnt)) #RE