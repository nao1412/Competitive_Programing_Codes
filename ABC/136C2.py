n = int(input())
h = list(map(int, input().split()))
ans ='Yes'
mah = 0
for i in h:
    mah = max(i, mah)
    if i < mah - 1:
        ans = 'No'
        break
print(ans)