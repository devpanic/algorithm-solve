import sys

data = int(sys.stdin.readline().rstrip())
print(data * (data - 1) * (data - 2) // 6)
print(3)