def main():
  n = int(input())
  s = input()
  memo = []
  for i in range(10):
    for j in range(10):
      for k in range(10):
        memo.append(str(i) + str(j) + str(k))
  ans = 0
  for i in memo:
    x = 0
    for j in range(n):
      if i[x] == s[j]:
        x += 1
        if x == 3:
          ans += 1
          break

  print(ans)

if __name__ == '__main__':
  main()