def lt(): return list(map(int, input().split()))
def mp(): return map(int, input().split())

def main():
  s = input()
  a = lt()
  a.sort(reverse=True)
  for i in a:
    s = s[:i] + '"' + s[i:]
  print(s)
  
  
if __name__ == '__main__':
  main()