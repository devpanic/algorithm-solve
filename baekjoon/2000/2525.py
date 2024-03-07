import sys

h, m = map(int, sys.stdin.readline().split())
to_add = int(sys.stdin.readline())
after_hour = (((to_add + m) // 60) + h) % 24
after_minute = (to_add + m) % 60
print(after_hour, after_minute)