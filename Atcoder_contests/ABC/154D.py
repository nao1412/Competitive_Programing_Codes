n, k = map(int, input().split())
p_bef = list(map(int, input().split()))
p_aft = []
a = 0
for i in range(n-k+1):
   for j in range(i, i+k):
      a += p_bef[j]
   p_aft.append(a)
   a = 0
p_aft2 = sorted(p_aft, reverse = True)
print((p_aft2[0]+k)/2)  