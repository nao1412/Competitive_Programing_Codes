h, w = map(int, input().split())
if h == 1 or w == 1:
    print(1)
else:
    if h*w % 2 == 0:
        print(h*w//2)
    else:
        print(h*w//2 + 1)