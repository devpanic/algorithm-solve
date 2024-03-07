import sys

max_line = 100
cur_line = 0
while cur_line < max_line:
    try:
        output_str = sys.stdin.readline()
        print(output_str, end="")
        cur_line += 1
    except:
        break