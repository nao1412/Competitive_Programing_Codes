n = int(input())
judge = 'Yes'
past_t = past_x = past_y = 0
for i in range(n):
    t, x, y = map(int,input().split())
    if t - past_t < x + y or ((t-past_t)-(x+y)) % 2 != 0:
        judge = 'No'
print(judge)
