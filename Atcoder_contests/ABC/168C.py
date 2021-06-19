import math

a,b,h,w = map(int, input().split())
if w == 0:
    c = abs(h*30-360)
else:
    c = min(abs(h*30-w*5.5), abs(w*5.5-h*30))

cosc = math.cos(math.radians(c))

print(math.sqrt(a**2 + b**2 - 2*a*b*cosc))