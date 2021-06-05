n = int(input())
a_bef = list(map(int, input().split()))
ans = 'YES'
a_aft = sorted(a_bef)
for i in range(n-1):
   if a_aft[i] == a_aft[i+1]:
      ans = 'NO'
      break
print(ans)