a, b, c, x, y = map(int, input().split())

l = a*x + b*y
m = max(x,y)*2*c
if x >= y:
    n = y*2*c + (x-y)*a
else:
    n = x*2*c + (y-x)*b

print(min(l,m,n))