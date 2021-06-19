def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7
dog = 10 ** 15 + 1

def main():
  n = int(input())
  alp = 'abcdefghijklmnopqrstuvwxyz'
  ans = ''
  while n > 0:
    n -= 1
    # ans += alp[n % 26]
    ans += chr(ord('a') + n % 26)
    n //= 26
  print(ans[::-1])

if __name__ == '__main__':
  main()