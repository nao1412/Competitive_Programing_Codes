def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  a, v = I()
  b, w = I()
  t = int(input())
  if v <= w:
    print('NO')
  else:
    if abs(a-b) <= (v-w)*t :
      print('YES')
    else:
      print('NO')

if __name__ == '__main__':
  main()