x = int(input())
if x == 2:
    print(2)
    exit()
if x%2 == 0:
    x += 1
flag = True
while flag:
    flag = False
    for i in range(2, int(x**0.5)+2):
        if x % i == 0:
            flag = True
            break
    ans = x
    x += 2
print(ans)