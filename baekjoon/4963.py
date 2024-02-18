import sys
sys.setrecursionlimit(10 ** 6)

col = -1
row = -1
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, 1, -1, 1, -1, 1, 0, -1]

def dfs(x, y):
    if graph[y][x] == 1:
        graph[y][x] = 0
    else:
        return False
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < col and 0 <= ny < row:
            dfs(nx, ny)
    return True

while True:
    col, row = map(int, sys.stdin.readline().split())

    if (col, row) == (0, 0):
        break
    
    graph = []
    for _ in range(row):
        graph.append(list(map(int, sys.stdin.readline().split())))
    result = 0

    for i in range(col):
        for j in range(row):
            if dfs(i, j):
                result += 1
    
    print(result)