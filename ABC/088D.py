from collections import deque

h ,w = map(int, input().split())
s = ['$'*(w+2)] * (h+2)
cnt = 0
for i in range(1,h+1):
    s[i] = '$' + input() + '$'
    cnt += s[i].count('.')

dist = [[-1]*(w+2) for _ in range(h+2)] # スタートからの距離の記録をするリスト
dist[1][1] = 0 # スタート地点を0 にする
q = deque()
q.append((1,1))
while q:
    x, y = q.popleft() # 探索地点を取り出す

    vx = [-1,0,1,0]
    vy = [0,-1,0,1]
    for i in range(4):
        nx = x + vx[i]
        ny = y + vy[i]
        if s[nx][ny] == '$' or s[nx][ny] == '#': continue # 壁なら通れないね！
        if dist[nx][ny] != -1: continue # もう最短距離がわかってるなら飛ばす
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny)) # 新しい地点の周りも探索したいからキューに入れておく

if dist[h][w] == -1:
    print(-1)
else:
    print(cnt - dist[h][w]-1)