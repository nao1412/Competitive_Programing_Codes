def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
from collections import deque
mod = 10**9 + 7

def main():
  h, w = I()
  ch, cw = I()
  dh, dw = I()
  s = ['$'*(w+4)]*(h+4)
  for i in range(h):
    s[i+2] = '$$' + input() + '$$'

  dist = [[-1]*(w+4) for _ in range(h+4)]
  dist[ch + 1][cw + 1] = 0
  q = deque()
  q.append((ch+1, cw+1))
  while q:
    x, y = q.popleft() # 探索地点を取り出す

    vx = [-1,0,1,0]
    vy = [0,-1,0,1]
    flag = [False, False, False, False]
    for i in range(4):
      nx = x + vx[i]
      ny = y + vy[i]
      if s[nx][ny] == '$': 
        flag[i] = True
        continue # 壁なら通れないね！
      if s[nx][ny] == '#':
        flag[i] = True
        continue
      if dist[nx][ny] != -1:
        if dist[nx][ny] > dist[x][y]:
          dist[nx][ny] = dist[x][y]
        flag[i] = True
        continue # もう最短距離がわかってるなら飛ばす
      dist[nx][ny] = dist[x][y]
      q.append((nx, ny)) # 新しい地点の周りも探索したいからキューに入れておく
    if not False in flag: # もし4つのflagがTrueの時5×5以内に飛べるか探す
      vvx = [-2,2,-2,-1,1,2,-2,-1,0,1,2,-2,-1,1,2,-2,-1,0,1,2]
      vvy = [0,0,-1,-1,-1,-1,-2,-2,-2,-2,-2,1,1,1,1,2,2,2,2,2]
      for i in range(20):
        nnx = x + vvx[i]
        nny = y + vvy[i]
        if s[nnx][nny] == '$': 
          continue # 壁なら通れないね！
        if s[nnx][nny] == '#':
          continue
        if dist[nnx][nny] != -1:
          if dist[nnx][nny] > dist[x][y] + 1:
            dist[nnx][nny] = dist[x][y] + 1
          continue # もう最短距離がわかってるなら飛ばす
        dist[nnx][nny] = dist[x][y] + 1
        q.append((nnx, nny))
  
  print(dist[dh+1][dw+1])

if __name__ == '__main__':
  main()