def main():
  m = int(input())
  a = [0]*m
  sign = []
  for i in range(m):
    a[i] = tuple(map(int ,input().split()))
  n = int(input())
  b = [0]*n
  for i in range(n):
    b[i] = tuple(map(int, input().split()))
  
  for i in range(m-1):
    dx = a[i+1][0] - a[i][0]
    dy = a[i+1][1] - a[i][1]
    sign.append((dx, dy))
  
  for i in range(n):
    x = 0
    plc = (b[i][0] + sign[x][0], b[i][1] + sign[x][1])
    while plc in b:
      x += 1
      if x == m-1:
        print(plc[0] - a[-1][0], plc[1] - a[-1][1])
        exit()
      plc = (plc[0] + sign[x][0], plc[1] + sign[x][1])

if __name__ == '__main__':
  main()