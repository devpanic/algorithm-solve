
# pypy 
import sys

n = int(sys.stdin.readline().strip())
dp_count = n - 2
depth = 0


def fibo_rec(num):
  global depth

  if num == 1 or num == 2:
    return

  depth += 1

  fibo_rec(num - 1)
  fibo_rec(num - 2)


fibo_rec(n)
print(depth + 1, dp_count)
