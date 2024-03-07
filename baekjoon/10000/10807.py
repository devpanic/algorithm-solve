import sys

n = int(sys.stdin.readline())
lists_n = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
print(lists_n.count(v))