import sys
sys.setrecursionlimit(1000)

n, depth = map(int, sys.stdin.readline().split())
result = []

def dfs():
    if len(result) == depth:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()
