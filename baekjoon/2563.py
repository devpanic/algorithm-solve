import sys

num_papers = int(sys.stdin.readline()[0:-1])
paper_set = []
results = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(num_papers):
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n, n + 10):
        for j in range(m, m + 10):
            results[i][j] = 1

for result in results:
    answer += result.count(1)

print(answer)