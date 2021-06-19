h, w = map(int , input().split())
s = [list(input()) for _ in range(h)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
           continue

        num = 0
        for k in range(8):
            ni = i + dx[k]
            nj = j + dy[k]

            if ni < 0 or h <= ni: continue
            if nj < 0 or w <= nj: continue
            if s[ni][nj] == '#': num += 1
        
        s[i][j] = str(num)
    
for i in range(h):
    print(''.join(s[i]))