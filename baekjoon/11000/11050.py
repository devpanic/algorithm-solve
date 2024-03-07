import sys

n, k = map(int, sys.stdin.readline().split())

upper = 1
lower = 1

for i in range(k + 1, n + 1):
    upper = upper * i

for i in range(1, n - k + 1):
    lower = lower * i

print(upper // lower)