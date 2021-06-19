def l(): return list(map(int, input().split()))
def m(): return map(int, input().split())

def main():
  c = [0]*3
  for i in range(3):
    c[i] = l()
  # for i in range(2):
  #   x = c[2][i+1] - c[2][i]
  #   for j in range(2):
  #     if c[j][i+1] - c[j][i] != x:
  #       print('No')
  #       exit()
  # print('Yes')

  a = [0]*3
  b = [0]*3
  b[0] = min(c[0])
  for i in range(3):
    a[i] = c[0][i] - b[0]
  for i in range(1,3):
    b[i] = c[i][0] - a[0]
  # print(a,b)
  for i in range(3):
    for j in range(3):
      if c[i][j] != a[j] + b[i]:
        print('No')
        exit()
  print('Yes')

  
if __name__ == '__main__':
  main()