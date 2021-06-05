def main():
  n = int(input())
  ha = [0]*n
  for i in range(n):
    xy = tuple(map(int, input().split()))
    ha[i] = xy

  h = set(ha)
  ans = 0
  for i in range(n-1):
    for j in range(i+1,n):
      dx = ha[i][0] - ha[j][0]
      dy = ha[i][1] - ha[j][1]
      l = dx**2 + dy**2
      if (ha[i][0] - dy, ha[i][1] + dx) in h and (ha[j][0] - dy, ha[j][1] + dx) in h:
        ans = max(ans, l)
      elif (ha[i][0] + dy, ha[i][1] - dx) in h and (ha[j][0] + dy, ha[j][1] - dx) in h:
        ans = max(ans, l)
      
  print(ans)

if __name__ == '__main__':
  main()