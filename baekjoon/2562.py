import sys
max_val = -1
max_index = -1

for i in range(1, 10):
    n = int(sys.stdin.readline())
    if n > max_val:
        max_val = n
        max_index = i

print(max_val)
print(max_index)