import sys

input_data = int(sys.stdin.readline().rstrip())
cur_div = 2

while input_data > 1:
    if input_data % cur_div == 0:
        print(cur_div)
        input_data = input_data / cur_div
    else:
        cur_div += 1
