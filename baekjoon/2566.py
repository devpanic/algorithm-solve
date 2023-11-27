import sys
max_x = 1
max_y = 1
max_val = 0

for i in range(9):
    cur_data = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if cur_data[j] > max_val:
            max_x = i + 1
            max_y = j + 1
            max_val = cur_data[j]

print(max_val)
print(max_x, max_y)