# 14425.py
# 이진 탐색으로 풀었는데, set() 사용하면 더 쉬울것 같다
# https://bba-dda.tistory.com/21
import sys

n, m = map(int, sys.stdin.readline().split())
s = []

for _ in range(n):
  s.append(sys.stdin.readline().strip())

s.sort()
count = 0
for _ in range(m):
  current_input = sys.stdin.readline().strip()
  start = 0
  end = n - 1
  while start <= end:
    target = (start + end) // 2
    if s[target] == current_input:
      count += 1
      break
    elif s[target] > current_input:
      end = target - 1
    else:
      start = target + 1

print(count)
