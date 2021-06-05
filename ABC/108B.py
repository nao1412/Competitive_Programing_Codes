x1, y1, x2, y2 = map(int, input().split())
xy = x2 - x1
yx = y1 - y2
print(x2+yx, y2+xy, x1+yx, y1+xy)