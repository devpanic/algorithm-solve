def dfs(start, graph, visited, num):
    visited[start] = True
    for i in range(num):
        if graph[start][i] == 1 and not visited[i]:
            dfs(i, graph, visited, num)

def solution(n, computers):
    graph = computers
    num = n
    visited = [False for _ in range(n)]
    result = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited, num)
            result += 1
            
    # print(result)
    return result