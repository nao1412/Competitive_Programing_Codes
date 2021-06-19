s = input()
n = len(s)
op = n - 1
ans = 0
for i in range(2**op):
  opm = [''] * op
  for j in range(op):
    if ((i >> j) & 1):
      opm[op - 1 - j] = '+'

  formula = ''
  for j in range(op):
    formula += s[j] + opm[j]
  formula += s[-1]
  ans += eval(formula)

print(ans)