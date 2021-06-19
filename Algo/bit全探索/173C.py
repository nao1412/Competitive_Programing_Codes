def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def I(): return int(input())
mod = 10**9 + 7

def main():
  h,w,k = MI()
  ans = 0
  s = []
  for i in range(h):
    s.append(input())
  for Is in range(1<<h):
    for Js in range(1<<w):
      cnt = 0
      for i in range(h):
        for j in range(w):
          if (Is>>i & 1): continue
          if (Js>>j & 1): continue
          if (s[i][j] == '#'): cnt += 1    
      if cnt == k: ans += 1
  print(ans)
if __name__ == '__main__':
  main()