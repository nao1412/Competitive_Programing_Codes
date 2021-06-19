def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  h, w, k = I()
  cnt = 0
  ans = 0
  c = [[] for _ in range(h)]
  for i in range(h):
    c[i] = input()
    for ww in range(w):
      if c[i][ww] == '#':
        cnt += 1
  if cnt < k:
    print(0)
    exit()

  for i in range(2**h):
    bit = [[0]*h, [0]*w]
    for j in range(h):
      if ((i >> j) & 1):
        bit[0][j] = 1
    for l in range(2**w):
      for m in range(w):
        if ((l >> m) & 1):
          bit[1][m] = 1
    
    for j in range(h):
      for l in range(w):
        if bit[0][j] == 1:
          for x in range(w):
            if c[j][x] == '#': hik += 1
        if bit[1][l] == 1:
          for x in range(h):
            if c[x][l] == '#' and x != j: hik += 1
    print(hik)
    if cnt - hik == k:
      ans += 1

  print(ans)

if __name__ == '__main__':
  main()