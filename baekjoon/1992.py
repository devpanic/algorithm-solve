import sys

sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline().strip())
table = []
result = ""

for _ in range(n):
  table.append(list(map(int, sys.stdin.readline().strip())))


def is_same(x, y, num):
  init_val = table[x][y]
  for i in range(x, x + num):
    for j in range(y, y + num):
      if table[i][j] != init_val:
        return False
  return True


def check(x, y, num):
  global result

  if is_same(x, y, num):
    result += str(table[x][y])
    return
  else:
    #재귀
    new_num = num // 2
    result += "("
    check(x, y, new_num)
    check(x, y + new_num, new_num)
    check(x + new_num, y, new_num)
    check(x + new_num, y + new_num, new_num)
    result += ")"


check(0, 0, n)
print(result)
