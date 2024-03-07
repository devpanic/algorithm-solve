import sys

num, instruction_count = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(num)]
sums = [[0 for _ in range(num + 1)] for _ in range(num + 1)]

for i in range(1, num + 1):
    sums[i][1:] = list(map(int, sys.stdin.readline().split()))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        sums[i][j] += sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1]

for i in range(instruction_count):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sums[x2][y2] - sums[x2][y1-1] - sums[x1 -1][y2] + sums[x1 - 1][y1 - 1])
