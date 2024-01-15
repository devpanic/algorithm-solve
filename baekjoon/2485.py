# 2485.py
# 간격간의 최대공약수 구하는 문제
# https://rileydev.tistory.com/45
import sys
from math import gcd

tree_count = int(sys.stdin.readline())
my_tree = []
gap = []

for _ in range(tree_count):
  my_tree.append(int(sys.stdin.readline()))

tree_count -= 1
gap = my_tree[-1] - my_tree[-2]

for i in range(tree_count - 1, 0, -1):
  temp_gap = my_tree[i] - my_tree[i - 1]
  gap = gcd(temp_gap, gap)

result = 0
# start_tree = min(my_tree)
# end_point = int(max(my_tree) / gap)

print(int((max(my_tree) - min(my_tree)) / gap - tree_count))
