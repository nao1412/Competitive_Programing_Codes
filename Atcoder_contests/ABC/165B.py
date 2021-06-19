x = int(input())
m = 100
cnt = 0
while m < x:
    m += int(m*0.01)
    cnt += 1
print(cnt)