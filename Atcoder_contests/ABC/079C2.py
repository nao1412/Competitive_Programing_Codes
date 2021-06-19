n = list(str(x) for x in input())
l = len(n)
op_cnt = l - 1
for i in range(2 ** op_cnt):
  op = ['-'] * op_cnt
  for j in range(op_cnt):
    if ((i >> j) & 1):
      op[op_cnt-1 - j] = '+'

  formula = ''
  for j in range(op_cnt):
    formula += n[j] + op[j]
  formula += n[op_cnt]
  if eval(formula) == 7:
    print(formula + '=7')
    break
