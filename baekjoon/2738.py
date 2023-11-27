import sys

n, m = map(int, sys.stdin.readline().split())
dataset_1 = [[0] * m for _ in range(n)]
dataset_2 = [[0] * m for _ in range(n)]

for i in range(n):
    dataset_1[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    dataset_2[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        print(dataset_1[i][j] + dataset_2[i][j], end=" ")
    print("")