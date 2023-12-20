import sys

x, y, width, height = map(int, sys.stdin.readline().split())

length_list = []
length_list.append((x - width) ** 2)
length_list.append(x ** 2)
length_list.append((y - height) ** 2)
length_list.append(y ** 2)

min_length = min(length_list)
print(int(min_length ** (1/2)))