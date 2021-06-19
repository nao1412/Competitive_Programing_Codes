k, n = map(int, input().split())
a = list(map(int, input().split()))

sans = [k-a[-1]+a[0]]

for i in range(n-1):
    sans.append(a[i+1]-a[i]) # 2つのリストから持ってくるから遅い
# print(sans)
print(sum(sans) - max(sans))
