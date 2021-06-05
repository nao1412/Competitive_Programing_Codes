def main():
  n = int(input())
  a = tuple(map(int ,input().split()))

  ans = [0]*(10**6)
  for x in a:
    ans[x-1] += 1
    ans[x] += 1
    ans[x+1] += 1
  print(max(ans))
if __name__ == '__main__':
  main()