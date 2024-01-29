# 18870.py
# ref https://gudwns1243.tistory.com/52
import sys

size = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
temp = list(set(input))
temp.sort()
result = dict()

for i in range(len(temp)):
  result[temp[i]] = i

for data in input:
  print(result[data], end=" ")
