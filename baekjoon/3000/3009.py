import sys

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

if x_list.count(x_list[0]) == 1:
    print(x_list[0], end=" ")
else:
    print(x_list[2], end=" ")

if y_list.count(y_list[0]) == 1:
    print(y_list[0])
else:
    print(y_list[2])