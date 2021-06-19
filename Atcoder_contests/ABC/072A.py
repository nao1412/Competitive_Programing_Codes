def main():
  x, t = map(int, input().split())
  if t > x:
    print(0)
  else:
    print(x-t)

if __name__ == '__main__':
  main()