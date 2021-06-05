n, a, b = map(int, input().split())

if abs(b-a)%2 == 0:
    print(abs(b-a)//2)
else:
    print(min((max(a,b)+min(a,b))//2, (2*n-max(a,b)-min(a,b)+1)//2))
    #min(a-1, n-b) + 1 +(b-a-1)//2
    