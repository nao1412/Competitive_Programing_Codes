x = int(input())
ans = 1
for i in range(1,int(x**0.5)+1):
    for j in range(2,x//2 + 1):
        if x >= i**j:
            ans = max(i**j, ans)


print(ans)