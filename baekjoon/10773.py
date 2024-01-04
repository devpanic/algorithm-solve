import sys

input_data_num = int(sys.stdin.readline().rstrip())
input_data_list = []

for _ in range(input_data_num):
    cur_data_num = len(input_data_list)
    cur_input = int(sys.stdin.readline().rstrip())

    if cur_input != 0:
        input_data_list.append(cur_input)
    else:
        input_data_list.pop()

print(sum(input_data_list))