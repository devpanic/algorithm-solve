import sys

sys.setrecursionlimit(10**6)

n, instructions, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
count = 1
visited = [0 for _ in range(n + 1)]

for _ in range(instructions):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(n + 1):
  graph[i].sort(reverse=True)


def dfs(node):
  global count
  if visited[node] != 0:
    count -= 1
    return

  visited[node] = count

  for i in graph[node]:
    count += 1
    dfs(i)
  return


dfs(start)
print('\n'.join(map(str, visited[1:])))
