# Bubble Sort
import sys

data_count = int(sys.stdin.readline().rstrip())
input_data_list = []

for _ in range(data_count):
    input_data_list.append(int(sys.stdin.readline().rstrip()))

for i in range(data_count - 1, 0, -1):
    for j in range(i):
        if input_data_list[i] < input_data_list[j]:
            temp = input_data_list[i]
            input_data_list[i] = input_data_list[j]
            input_data_list[j] = temp

for i in range(data_count):
    print(input_data_list[i])