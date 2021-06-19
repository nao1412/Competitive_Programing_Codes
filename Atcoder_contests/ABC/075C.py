def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n,m = I()
  gragh = [[] for _ in range(n)]
  for i in range(n):
    a, b = I()
    gragh[a-1].append(b-1)
    gragh[b-1].append(a-1)
  visited = []
  
if __name__ == '__main__':
  main()