def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  h, w, k = I()
  ans = 0
  c = [[] for _ in range(h)]
  x, y = [0]*w, [0]*h
  for i in range(h):
    c[i] = input()
  for i in range(h):
    for j in range(w):
      if c[i][j] == '#':
        x[j] += 1
        y[i] += 1
  
  for i in range(2**h):
    ybit = [0]*h
    for j in range(h):
      if ((i >> j) & 1):
        ybit[j] = 1
    for l in range(2**w):
      xbit = [0]*w
      for m in range(w):
        if((l >> m) & 1):
          xbit[m] = 1

      xx, yy = 0, 0
      for xxx in range(h):
        for yyy in range(w):
          if ybit[xxx]: yy += y[xxx]
          if xbit[yyy]: xx += x[yyy]
      pp = max(xx, yy)-min(xx,yy)
      print(xbit, ybit, pp, xx, yy)
      if pp == k:
        ans += 1
  print(ans)
if __name__ == '__main__':
  main()