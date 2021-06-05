a, b, c = map(int, input().split())
k = int(input())
s =  max(a,b,c) * (2**k)
print(a+b+c+s-max(a,b,c))