n = int(input())
a = n//1.08
b = 1+a
if int(a*1.08) == n:
    print(int(a))
elif int(b*1.08) == n:
    print(int(b))
else:
    print(':(')
    