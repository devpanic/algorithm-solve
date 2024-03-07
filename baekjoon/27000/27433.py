import sys

sys.setrecursionlimit(1000)

def factorial(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n - 1)

input = int(sys.stdin.readline())

print(factorial(input))
