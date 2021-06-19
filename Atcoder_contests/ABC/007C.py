from collections import deque

r,c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
css = [0]*r
for i in range(r):
    css[i] = list(input()) # 縦h * 横h

que = deque()
dist = [[-1]*c for _ in range(r)]
sxi, syi = sx-1, sy-1
dist[sxi][syi] = 0
que.append((sxi, syi))
#幅優先探索
while que: # キューに要素が入っている間は続ける
    x, y = que.popleft()

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]: # 上下左右の移動
        nx, ny = x + dx, y + dy
        # if not 0 <= nx < r or not 0 <= ny < c: continue
        if css[nx][ny] == '#': continue # 壁なら無視 distには-1のまま
        if dist[nx][ny] != -1: continue # すでに探索済みなら飛ばす
        dist[nx][ny] = dist[x][y] + 1 # 移動先に 前+1 最短を書き込む
        que.append((nx, ny)) # キューに発見した場所を登録し、次の探索の場所となる

print(dist[gy-1][gx-1]) # ゴール地点の最短距離を代入
