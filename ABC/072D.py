def main():
  n = int(input())
  p = tuple(map(int ,input().split()))
  
  memo = [0]*n
  for i in range(n):
    if i+1 != p[i]:
      memo[i] = i+1 - p[i]
  for i in range(n):
    

  
  print(ans)
if __name__ == '__main__':
  main()