import sys

input_data = int(sys.stdin.readline().rstrip())
curr_line = 1

while True:
    if input_data <= curr_line:
        if curr_line % 2 == 0:
            print(input_data, "/", curr_line - input_data + 1, sep="")
        else:
            print(curr_line - input_data + 1, "/", input_data, sep="")
        break
    else:
        input_data = input_data - curr_line
        curr_line += 1