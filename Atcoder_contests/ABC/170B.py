def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  x , y = I()
  for i in range(x+1):
    if 2 * i + 4 * (x-i) == y:
      print('Yes')
      exit()
    
  print('No')
  
if __name__ == '__main__':
  main()