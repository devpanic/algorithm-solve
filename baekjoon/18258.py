import sys

input_total_instruction = int(sys.stdin.readline().rstrip())
data_list = []
current_head = 0
len_data = 0

for _ in range(input_total_instruction):
    current_instruction = list(sys.stdin.readline().split())
    match current_instruction[0]:
        case "push":
            data_list.append(int(current_instruction[1]))
            len_data += 1
        case "pop":
            if len_data == 0:
                print(-1)
            else:
                print(data_list[current_head])
                current_head += 1
                len_data -= 1
        case "size":
            print(len_data)
        case "empty":
            if len_data == 0:
                print(1)
            else:
                print(0)
        case "front":
            if len_data == 0:
                print(-1)
            else:
                print(data_list[current_head])
        case "back":
            if len_data == 0:
                print(-1)
            else:
                print(data_list[len(data_list) - 1])