''' GCD ''' 

''' 再起関数 '''
def GCD(a, b):
  if b == 0: return a
  else: return gcd(b, a%b)

''' ユークリッドの互除法 '''
def GCD(a, b):
  while b:
    a, b = b, a%b
  return a


''' LCM '''

''' from GCD '''
def LCM(a, b):
  return a*b // GCD(a, b)

''' 再起関数 '''
def LCM(a, b):
  remind = a % b
  if remind == 0: return a
  return a* LCM(b, remind) // remind
