def main():
  f = open('input.txt', 'r')
  data = f.readlines()
  memo = []
  for i in range(len(data)):
    data[i] = data[i].strip()
    if i != len(data)-1:
      i, s = data[i].split(':')
      memo.append([int(i),s])
      # print(i, s)
    else: num = int(data[i])
  memo = sorted(memo, key=lambda x:x[0])
  # print(memo)
  ans = ''
  flag = True
  for i in range(len(memo)):
    if num % memo[i][0] == 0:
      flag = False
      ans += memo[i][1]
  if flag: print(num)
  else: print(ans)

if __name__ == '__main__':
  main()

# pfXvTAYBYjEAuamAEasFqMSrwrRSN6