import sys

input_data_sum = int(sys.stdin.readline().rstrip())

for _ in range(input_data_sum):
    cur_input = sys.stdin.readline().rstrip()
    total_VPS = 0

    for i in range(len(cur_input)):
        if cur_input[i] == "(":
            total_VPS += 1
        elif cur_input[i] == ")":
            total_VPS -= 1
            if total_VPS < 0:
                break
            
    if total_VPS != 0:
        print("NO")
    else:
        print("YES")