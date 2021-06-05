k = int(input())
ans = 'OK'
a, b = map(int, input().split())
if b-a+1 >= k:
    ans = 'OK'
else:
    for i in range(a, b+1):
        if i%k == 0:
            ans = 'OK'
            break
        else:
            ans = 'NG'
print(ans)