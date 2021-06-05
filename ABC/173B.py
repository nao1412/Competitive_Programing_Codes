def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  ac, wa, tle, re = 0,0,0,0
  s = []
  for _ in range(n):
    s.append(input())
  for i in range(n):
    if s[i] == 'AC':
      ac += 1
    elif s[i] == 'WA':
      wa += 1
    elif s[i] == 'TLE':
      tle += 1
    else:
      re += 1
  print('AC x', ac)
  print('WA x', wa)
  print('TLE x', tle)
  print('RE x', re)

  
if __name__ == '__main__':
  main()