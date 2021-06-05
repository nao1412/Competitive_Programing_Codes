a, b = map(int, input().split())
ans = 0
for i in range(a, b+1):
    i = str(i)
    cnt = 1
    for j in range((len(i)//2)+1):
        if i[j] != i[-j-1]:
            cnt = 0
            break
    ans += cnt
print(ans)