a,b,c,d = map(int, input().split())

if (a-c)**2 - (b-d)*8 < 0:
    print('No')
elif (a-c)**2 - (b-d)*8 == 0:
    print('Yes')
else:
    print((a+c)/2, (b+d)/2)