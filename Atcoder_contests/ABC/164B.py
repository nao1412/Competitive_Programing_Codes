import math
a, b, c, d = map(int, input().split())
taka = math.ceil(a/d)
ao = math.ceil(c/b)
if taka >= ao:
    print('Yes')
else:
    print('No') 