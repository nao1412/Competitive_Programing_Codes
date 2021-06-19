#ABC 130C
w, h, x, y = map(int, input().split())
ans_1 = w*h/2
if x == w/2 and y == h/2:
   ans_2 = 1*True
else:
   ans_2 = 1*False
print(ans_1, ans_2)