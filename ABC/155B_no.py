n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i%2 == 0:
        if i%3 == 0 or i%5 == 0:
            ans = 'APPROVED'
        else:
            ans = 'DENIED'
            break
print(ans) #breakではだめだった