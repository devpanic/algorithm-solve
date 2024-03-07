import sys

num_instruction = int(sys.stdin.readline().rstrip())
stack_list = []

for _ in range(num_instruction):
    current_instruction = list(map(int, sys.stdin.readline().split()))
    stack_size = len(stack_list)
    match current_instruction[0]:
        case 1:
            stack_list.append(current_instruction[1])
        case 2:
            if stack_size != 0:
                print(stack_list.pop())
            else:
                print(-1)
        case 3:
            print(stack_size)
        case 4:
            if stack_size == 0:
                print(1)
            else:
                print(0)
        case 5:
            if stack_size != 0:
                print(stack_list[stack_size - 1])
            else:
                print(-1)
