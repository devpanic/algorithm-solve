import sys

n, k = map(int, sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))
sum = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    sum[i] = sum[i - 1] + input[i - 1]

max = -100 * (n + 1)

for i in range(1, n - k + 2):
    temp = sum[i + k - 1] - sum[i - 1]
    if max < temp:
        max = temp

print(max)