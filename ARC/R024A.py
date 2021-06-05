def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())

def main():
  l, r = I()
  l = LI()
  r = LI()
  memol = [0]*31
  memor = [0]*31
  for i in range(10,41):
    memol[i-10] = l.count(i)
    memor[i-10] = r.count(i)
  ans = 0
  for i in range(31):
    ans += min(memol[i], memor[i])

  print(ans)  
if __name__ == '__main__':
  main()