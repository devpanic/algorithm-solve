import sys

n, m = map(int, sys.stdin.readline().split())
info = {}

for _ in range(n):
    info[sys.stdin.readline().strip()] = True

count = 0
result = []
for _ in range(m):
    cur_info = sys.stdin.readline().strip()
    if cur_info in info:
        count += 1
        result.append(cur_info)

print(count)
result.sort()
for print_info in result:
    print(print_info)