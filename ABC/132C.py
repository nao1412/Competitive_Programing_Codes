#ABC 135C
n = int(input())
d = list(map(int, input().split()))
ans = 0
d.sort()
k = d[int(n/2)]
while k > d[int(n/2)-1]:   #d[n//2] - d[n//2 - 1] でいける　この差が答え
   k -= 1
   ans += 1
print(ans)