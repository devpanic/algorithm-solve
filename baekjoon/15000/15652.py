import sys

sys.setrecursionlimit(1000)

n, depth = map(int, sys.stdin.readline().split())
result = []


def dfs(k):
  if len(result) == depth:
    print(' '.join(map(str, result)))
    return
  for i in range(k, n + 1):
    result.append(i)
    dfs(i)
    result.pop()


dfs(1)