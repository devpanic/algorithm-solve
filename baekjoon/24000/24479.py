import sys
sys.setrecursionlimit(10 ** 6)

n, m, start_node = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort()
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(start_node)
print('\n'.join(map(str, visited[1:])))
