def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())

def main():
  s = input()
  ans = 0
  for i in range(len(s)):
    if i % 2 == 0:
      ans += int(s[i])
    else:
      ans -= int(s[i])
    
  print(ans)

  
if __name__ == '__main__':
  main()