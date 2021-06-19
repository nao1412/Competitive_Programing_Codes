n = int(input())
c = 1
for i in range(1,int(n**0.5) + 1):
    if n%i == 0:
        c = max(c,i)

print(n//c +c -2)