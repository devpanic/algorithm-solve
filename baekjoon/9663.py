# https://seongonion.tistory.com/103
import sys

sys.setrecursionlimit(1000)

n = int(sys.stdin.readline().strip())
result = 0
chess = [0] * n
column = [False] * n


def check(x):
  for i in range(x):  # i = 퀸을 놓은 세로 위치
    if chess[i] == chess[x] or abs(chess[i] - chess[x]) == abs(i - x):
      return False

  return True


def n_queen(x):
  global result
  if x == n:
    result += 1
    return

  for j in range(n):  # j = 퀸을 놓은 가로 위치
    if column[j]:
      continue
    chess[x] = j
    if check(x):
      column[j] = True
      n_queen(x + 1)
      column[j] = False


n_queen(0)
print(result)
