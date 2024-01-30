# 2798.py
import sys

n, m = map(int, sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))
max = -1
sum = 0
result = []
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum = input[i] + input[j] + input[k]
      result.append(sum)
      if sum <= m and sum >= max:
        max = sum

print(max)
