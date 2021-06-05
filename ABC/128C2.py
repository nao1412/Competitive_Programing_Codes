def main():
  n, m = map(int,input().split())
  light = [[0]*n for _ in range(m)]
  for i in range(m):
    kk = list(map(int, input().split()))
    k = kk.pop(0)
    for j in range(k):
      light[i][kk[j]-1] = 1
  p = list(map(int, input().split()))

  ans = 0
  for i in range(2**n): # switchのbit
    sw = [0]*n
    for j in range(n):
      if ((i >> j) & 1):
        sw[j] = 1

    flag = True
    for j in range(m):
      cnt = 0
      for k in range(n):
        if sw[k] == 1 and light[j][k] == 1:
          cnt += 1
      if cnt % 2 != p[j]:
        flag = False
        break
    if flag:
      ans += 1
    
  print(ans)

if __name__ == '__main__':
  main()