# 10814.py
import sys

count = int(sys.stdin.readline())
input = []
names = [[] for _ in range(201)]

for _ in range(count):
  id, name = sys.stdin.readline().split()
  names[int(id)].append(name)

for i in range(1, 201):
  if len(names[i]) > 0:
    for j in range(len(names[i])):
      print(i, names[i][j])
