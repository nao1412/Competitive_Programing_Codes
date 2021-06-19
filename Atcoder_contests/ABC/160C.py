#160C
k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(k+a[0])
b = [a[i+1]-a[i] for i in range(n)]
print(k-max(b))