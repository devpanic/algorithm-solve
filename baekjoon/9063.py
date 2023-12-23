import sys

num_dataset = int(sys.stdin.readline().rstrip())
x_list = []
y_list = []

for _ in range(num_dataset):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))