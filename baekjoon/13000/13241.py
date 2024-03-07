import sys

a, b = map(int, sys.stdin.readline().split())

origin_a = a
origin_b = b

while b > 0:
    a, b = b, a % b

print(int(origin_a * origin_b / a))