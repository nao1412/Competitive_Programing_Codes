h, w = map(int, input().split())
s = ['.'*(w+2)]
for i in range(h):
  ss = '.' + input() + '.'
  s.append(ss)
s.append('.'*(w+2))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(h):
  for j in range(w):
    cnt = 0
    for k in range(4):
      yi = i + dy[k]
      xi = j + dx[k]
      if s[i][j] == '#' and s[yi][xi] == '.':
        cnt += 1
    if cnt == 4:
      print('No')
      exit()

print('Yes')
