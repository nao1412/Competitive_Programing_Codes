def _rot13(c, i):
  if 'A' <= c and c <= 'Z':
    return chr((ord(c) - ord('A') + i) % 26 + ord('A'))
  
  if 'a' <= c and c <= 'z':
    return chr((ord(c) - ord('a') + i) % 26 + ord('a'))
  
  return c # それ以外の文字はそのまま

def rot13(s, i):
  g = (_rot13(c, i) for c in s)
  return ''.join(g)

def main():
  s = input()
  # for i in range(1, 26):
  #   print(rot13(s, i))
  print(rot13(s, 13))
  import codecs
  print(codecs.decode(s, 'rot13'))

if __name__ == '__main__':
  main()