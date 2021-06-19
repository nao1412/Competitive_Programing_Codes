def main():
  s = input()
  if s.count('a') == 1 and s.count('b') == 1 and s.count('c') == 1:
    print('Yes')
  else:
    print('No')

if __name__ == '__main__':
  main()